from flask import render_template
import sqlite3 as sql


def read_data(SQL,id):
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute(SQL,id)
    data = cur.fetchall()
    return render_template("index.html", datas=data)