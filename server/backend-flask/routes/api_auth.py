from flask import current_app as app


def validate_auth_token(token):
    return token == app.config['API_KEY']
