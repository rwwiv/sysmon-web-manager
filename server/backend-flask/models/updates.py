from models import db
from models.sysmon import Sysmon
from models.sysmon_config import SysmonConfig


class Updates(db.Model):
    agent = db.Column(db.String(36), db.ForeignKey('agent.uuid'), primary_key=True)
    config = db.Column(db.String(250), db.ForeignKey(SysmonConfig.name))
    sysmon = db.Column(db.String(20), db.ForeignKey(Sysmon.version))
