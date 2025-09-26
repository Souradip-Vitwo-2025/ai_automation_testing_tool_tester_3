import sqlite3

def get_user_orders(user_id):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # Intentional typo in table/column names for testing
    cursor.execute("SELECT id, usernamee FROM usrs WHERE id = ?", (user_id,))
    results = cursor.fetchall()

    conn.close()
    return results

def insert_order(user_id, product, amount):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    # Correct SQL
    cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (user_id, product, amount))
    conn.commit()

    conn.close()
