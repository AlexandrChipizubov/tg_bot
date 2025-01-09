import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def df_connect() -> None:
    cursor.execute("CREATE TABLE IF NOT EXISTS expense(id integer, amount integer, raw_text text)")
    conn.commit()

def insert(amount, category_text) -> int:
    cursor.execute('SELECT COALESCE(MAX(id), -1) FROM expense')
    id = cursor.fetchall()
    id = id[0][0] + 1
    cursor.execute("INSERT INTO expense VALUES (?, ?, ?)", (id, amount, category_text))
    conn.commit()
    return id

def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"DELETE FROM {table} WHERE id={row_id}")
    conn.commit()

def get_cursor():
    return cursor