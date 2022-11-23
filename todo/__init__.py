from flask import Flask
from . import db
from todo.routes import bp

def create_app():
    app = Flask(__name__)

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['DATABASE'] = 'todo/database.db'

    db.init_app(app)
    app.register_blueprint(bp)
    return app
