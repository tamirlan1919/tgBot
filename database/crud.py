import sqlite3

def insert_to_table_user(telegram_id, username, created_at):
    with sqlite3.connect('telegram.db') as conn:
        cursor = conn.cursor() #SQL запросов
        cursor.execute('''
    INSERT INTO users(telegram_id, username, created_at)
    VALUES(?, ?, ?)
''', (telegram_id, username, created_at))
        conn.commit()


def select_user_by_id(telegram_id):
    with sqlite3.connect('telegram.db') as conn:
        cursor = conn.cursor() #SQL запросов
        cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
        user = cursor.fetchone()
        return user or None