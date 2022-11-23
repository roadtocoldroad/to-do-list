from flask import  request, redirect, url_for
from flask.blueprints import Blueprint
import sqlite3 as sql
from . import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/',methods = ['GET'])
def read():
    return db.read_data("select * from todo",'')


@bp.route('/',methods = ['POST'])
def post():
        title = request.form['title']
        url = request.url
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("insert into todo(title,url) values (?,?)", (title, url))
        con.commit()
        return redirect(url_for("main.post"))


@bp.route('/<string:todo_id>')
def find_todo_by_id(todo_id):
   return db.read_data("select * from todo where todo_id=?", todo_id)