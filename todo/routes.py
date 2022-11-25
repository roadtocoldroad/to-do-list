import json

from flask import  request
from flask.blueprints import Blueprint
from todo.db import get_db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/',methods = ['GET'])
def read():
    todo_list = []
    db = get_db()
    fetch_data = db.execute("select * from todo").fetchall()

    for row in fetch_data:
        todo_id = row['todo_id']
        todo_list.append({
            'id' : todo_id,
            'title' : row['title'],
            'completed': row['completed'],
            'url': row['url'] + str(todo_id)
          })

    return json.dumps(todo_list,ensure_ascii=False)


@bp.route('/',methods = ['POST'])
def post():
    params = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("insert into todo(TITLE,URL) values (?,?)", (params['title'], request.url))
    db.commit()
    post_id = cursor.lastrowid
    return find_todo_by_id(post_id)


@bp.route('/<string:todo_id>')
def find_todo_by_id(todo_id):
    found_list = []
    db = get_db()
    fetch_data = db.execute(
        "select * from todo where todo_id = ?", (todo_id,)
    ).fetchall()

    for row in fetch_data:
        found_list.append({
            'id': row['todo_id'],
            'title': row['title'],
            'completed': row['completed'],
            'url': row['url'] + str(todo_id)
        })
        return json.dumps(found_list,ensure_ascii=False)

