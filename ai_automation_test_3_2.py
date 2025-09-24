# test_sql_syntax_bug.py

import sqlite3

def get_students():
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()

    # BUG: "FORM" is a typo, should be "FROM"
    query="SELECT name, marks FORM Students WHERE marks > 50"
    cur.execute(query)

    rows=cur.fetchall()
    print("Students:", rows)

    conn.close()
