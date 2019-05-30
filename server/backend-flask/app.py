import os
from datetime import datetime, timedelta

from flask import Flask
from flask_apscheduler import APScheduler
from flask_socketio import SocketIO
from scheduler import jobs, scheduler
from models import db
from models.auth import user
from flask_user import UserManager
from routes import heartbeat


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # init ORM
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # init user manager
    user_manager = UserManager(app, db, user.User)

    # register blueprints
    app.register_blueprint(heartbeat.blueprint, url_prefix='/heartbeat')

    # init scheduler
    scheduler.init_app(app)
    scheduler.start()

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.app_context().push()
    socketio = SocketIO(flask_app)

    socketio.run(app=flask_app, host='0.0.0.0', port=8080)
