from models import db


class SysmonConfig(db.Model):
    name = db.Column(db.String(250), primary_key=True)
