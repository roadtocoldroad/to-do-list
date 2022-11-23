from flask import  request, redirect, url_for
from flask.blueprints import Blueprint
import sqlite3 as sql
from . import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        url = request.url
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("insert into todo(TITLE,URL) values (?,?)", (title, url))
        con.commit()
        return redirect(url_for("main.index"))
    return db.read_data("select * from todo",'')


@bp.route('/<string:todo_id>')
def read_by_id(todo_id):
   return db.read_data("select * from todo where todo_id=?", todo_id)
