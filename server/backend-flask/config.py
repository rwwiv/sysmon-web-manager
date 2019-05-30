DEBUG = True
DEVELOPMENT = False
# Keys
SECRET_KEY = 'dev'
API_KEY = 'secret'
CSRF_ENABLED = True

# ORM flags
SQLALCHEMY_DATABASE_URI = 'sqlite:///backend-flask.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User auth flags
USER_APP_NAME = 'Sysmon Web Manager'  # Shown in email templates and page footers
USER_ENABLE_EMAIL = False  # Disable email authentication
USER_ENABLE_USERNAME = True  # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form
USER_EMAIL_SENDER_EMAIL = 'william.wernert@securityonionsolutions.com'

APPLICATION_ROOT = '/apiv1'

JOBS = [
    {
        'id': 'update_agent_status',
        'func': 'scheduler.jobs:update_agent_status',
        'trigger': 'interval',
        'seconds': 10
    }
]
