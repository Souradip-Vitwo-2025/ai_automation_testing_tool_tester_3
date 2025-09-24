# test_sql_bug.py

import sqlite3

def check_pass_students():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()

    # Syntactically valid but semantically wrong for the task
    query = "UPDATE Students SET marks='Pass' WHERE marks>50"
    cur.execute(query)

    # Intended was a SELECT, not UPDATE
    rows = cur.fetchall()
    print("Students who passed:", rows)

    conn.close()
