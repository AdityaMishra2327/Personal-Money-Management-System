import sqlite3

def create_connection():
    conn = sqlite3.connect('expenses.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_expense(description, amount, date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)',
                   (description, amount, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

create_table()
