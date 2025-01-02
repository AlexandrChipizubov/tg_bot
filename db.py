import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def df_connect() -> None:
    cursor.execute("CREATE TABLE IF NOT EXISTS expense(amount integer, raw_text text)")
    conn.commit()

def insert(amount, category_text):
    cursor.execute("INSERT INTO expense VALUES (?, ?)", (amount, category_text))
    conn.commit()

def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"DELETE FROM {table} WHERE amount={row_id}")
    conn.commit()

def get_cursor():
    return cursor