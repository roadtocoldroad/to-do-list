from flask import Flask
from todo.app import bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.register_blueprint(bp)
    return app
