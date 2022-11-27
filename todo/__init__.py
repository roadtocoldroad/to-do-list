from flask import Flask
from . import db
from todo.routes import bp
import os

def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("to_do_list_key")
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['DATABASE'] = 'todo/database.db'

    db.init_app(app)
    app.register_blueprint(bp,url_prefix='/')
    return app
