import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS todo")

sql =   '''
    create table "todo" (
    "todo_id" INTEGER PRIMARY KEY AUTOINCREMENT,
     "title" text, 
     "completed" bool default false, 
     "url" text)
    '''

cur.execute(sql)
con.commit()
con.close()