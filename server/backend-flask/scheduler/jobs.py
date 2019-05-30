from datetime import datetime, timedelta

from models import db
from models.agent import Agent
from models.enums import StatusTypes
from scheduler import scheduler


def update_agent_status():
    with scheduler.app.app_context():
        all_agents = Agent.query.all()
        current_time = datetime.now()

        if all_agents is not None:
            for agent in all_agents:
                time_diff = (agent.last_contact - current_time) / timedelta(minutes=1)
                if time_diff > 60:
                    agent.agent_status = StatusTypes.OFFLINE
                    db.session.add(agent)

            db.session.commit()
