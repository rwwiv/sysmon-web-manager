from models import db
from models.enums import ExternalLinks


class Links(db.Model):
    link_type = db.Column(db.Enum(ExternalLinks))
    link_value = db.Column(db.String(250))
