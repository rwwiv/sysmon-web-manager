from models import db


class Sysmon(db.Model):
    version = db.Column(db.String(250), primary_key=True)
    current = db.Column(db.Boolean, nullable=False)
