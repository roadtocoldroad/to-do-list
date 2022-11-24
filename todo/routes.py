import json

from flask import  request, redirect, url_for , jsonify
from flask.blueprints import Blueprint
from flask import render_template
from todo.db import get_db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/',methods = ['GET'])
def read():
    todo_list = []
    db = get_db()
    fetch_data = db.execute("select * from todo").fetchall()

    for row in fetch_data:
         todo_list.append({
            'id' : row[0],
            'title' : row[1],
            'completed': row[2],
            'url': row[3]
          })

    return json.dumps(todo_list,ensure_ascii=False)


@bp.route('/',methods = ['POST'])
def post():
    db = get_db()
    db.execute(
        "insert into todo(TITLE,URL) values (?,?)",
        (request.form['title'], request.url)
    )
    db.commit()
    return redirect(url_for("main.post"))


@bp.route('/<string:todo_id>')
def find_todo_by_id(todo_id):
    found_list = []

    db = get_db()
    fetch_data = db.execute(
        "select * from todo where todo_id = ?", (todo_id,)
    ).fetchall()

    for row in fetch_data:
        found_list.append({
            'id': row[0],
            'title': row[1],
            'completed': row[2],
            'url': row[3]
        })
        return json.dumps(found_list,ensure_ascii=False)

