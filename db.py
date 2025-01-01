import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def df_connect() -> None:
    cursor.execute("CREATE TABLE IF NOT EXISTS expense(amount integer, raw_text text)")
    conn.commit()