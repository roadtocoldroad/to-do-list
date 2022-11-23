from flask import render_template
import sqlite3 as sql
from flask import current_app
from flask import g



def get_db():
    if "db" not in g:
        g.db = sql.connect(current_app.config['DATABASE'])
        g.db.row_factory = sql.Row
    return g.db

def close_db(e=None):
    db = g.pop('db',None)

    if db is not None:
        db.close()


def read_data(SQL,id):
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute(SQL,id)
    data = cur.fetchall()
    return render_template("index.html", datas=data)

