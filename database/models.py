import sqlite3

def make_table_user():
    with sqlite3.connect('telegram.db') as conn:
        cursor = conn.cursor() #SQL запросов
        cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY,
                       telegram_id TEXT,
                       username TEXT,
                       created_at DATETIME
                       )
''')
        conn.commit() #Чтобы применить изменения в БД

