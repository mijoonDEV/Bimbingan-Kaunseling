import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    student_id TEXT,
    date TEXT,
    time TEXT,
    topic TEXT,
    notes TEXT
)
""")

conn.commit()
conn.close()
