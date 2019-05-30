from datetime import datetime
from flask import Blueprint, request, jsonify
from models import db
from models.enums import StatusTypes, ActionTypes
from models.agent import Agent
from models.updates import Updates
from routes.api_auth import validate_auth_token
from routes.constants import *


blueprint = Blueprint('heartbeat', __name__)


@blueprint.route('/', methods=['POST'])
def ping():
    return 'pong', 200


@blueprint.route('/create_agent/<uuid>', methods=['POST'])
def create_agent(uuid):
    if not validate_auth_token(request.headers.get(AUTH_TOKEN_KEY_NAME)):
        return jsonify({'message': UNAUTHORIZED_ERR}), 401
    elif Agent.query.get(uuid) is not None:
        return jsonify({'message': f'ERROR: Agent with uuid: ${uuid} already exists.'}), 400
    else:
        content = request.get_json(silent=True)
        if content is None:
            return jsonify({'message': INVALID_JSON_ERR}), 400
        hostname = content.get('hostname')

        if hostname is None:
            return jsonify({'message': INVALID_JSON_ERR}), 401

        agent_status = StatusTypes.NEW
        sysmon_status = StatusTypes.NEW

        new_agent = Agent(
            uuid=uuid,
            hostname=hostname,
            ip_address=request.remote_addr,
            agent_status=agent_status,
            last_contact=datetime.now(),
            sysmon_status=sysmon_status
        )

        db.session.add(new_agent)
        db.session.commit()
        return jsonify({
            'message': 'SUCCESS: New agent created',
            'agent_information': new_agent
        }), 200


@blueprint.route('/update_agent/<uuid>', methods=['PUT'])
def update_agent(uuid):
    if not validate_auth_token(request.headers.get(AUTH_TOKEN_KEY_NAME)):
        return jsonify({'message': UNAUTHORIZED_ERR}), 401

    else:
        agent = Agent.query.get(uuid)

        if agent is None:
            return jsonify({'message': f'Agent with uuid: ${uuid} was not found'}), 404

        else:
            content = request.get_json(silent=True)

            # update values if they exist in the json request
            agent.hostname = content.get('hostname', agent.hostname)
            agent.ip_address = request.remote_addr  # always update the IP address
            agent.agent_status = StatusTypes.ONLINE
            agent.sysmon_version = content.get('sysmon_status', agent.sysmon_version)
            agent.config_name = content.get('config_name', agent.config_name)
            agent.sysmon_status = content.get('sysmon_status', agent.sysmon_status)
            agent.sysmon_last_running = content.get('sysmon_last_running', agent.sysmon_last_running)

            if agent.pending_action is None:
                save_agent(agent)
                return 'pong', 200

            else:
                action = agent.pending_action
                agent.pending_action = None
                response = {'action': action}

                if action == ActionTypes.INSTALL or agent.pending_action == ActionTypes.UPDATE:
                    update_values = Updates.query.get(agent=uuid)
                    if update_values.sysmon is not None:
                        response['sysmon_version'] = update_values.sysmon
                    if update_values.config is not None:
                        response['config_name'] = update_values.config

                save_agent(agent)
                return jsonify(response), 200


def save_agent(agent):
    db.session.add(agent)
    db.session.commit()
