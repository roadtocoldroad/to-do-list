from flask import Flask,render_template,request,redirect,url_for,jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        url = request.url
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("insert into todo(TITLE,URL) values (?,?)", (title, url))
        con.commit()
        return redirect(url_for("index"))
    return read_data("select * from todo",'')


@app.route('/<string:todo_id>')
def read_by_id(todo_id):
   return read_data("select * from todo where todo_id=?", todo_id)

def read_data(SQL,id):
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute(SQL,id)
    data = cur.fetchall()
    return render_template("index.html", datas= data)

if __name__ == '__main__':
 app.secret_key = 'super secret key'
 app.config['SESSION_TYPE'] = 'filesystem'
 app.run()

