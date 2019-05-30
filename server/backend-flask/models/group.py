from models import db
from models.sysmon_config import SysmonConfig
from models.sysmon import Sysmon


class Group(db.Model):
    name = db.Column(db.String(250), primary_key=True)
    config = db.Column(db.String(250), db.ForeignKey(SysmonConfig.name))
    sysmon = db.Column(db.String(20), db.ForeignKey(Sysmon.version))
