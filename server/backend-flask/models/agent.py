from models import db
from models.enums import StatusTypes
from models.sysmon_config import SysmonConfig
from models.sysmon import Sysmon


class Agent(db.Model):
    uuid = db.Column(db.String(36), primary_key=True)
    hostname = db.Column(db.String(250), nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)
    agent_status = db.Column(db.Enum(StatusTypes), nullable=False)
    last_contact = db.Column(db.DateTime, nullable=False)
    sysmon_version = db.Column(db.String(20), db.ForeignKey(Sysmon.version))
    config_name = db.Column(db.String(250), db.ForeignKey(SysmonConfig.name))
    sysmon_status = db.Column(db.Enum(StatusTypes), nullable=False)
    sysmon_last_running = db.Column(db.DateTime)

