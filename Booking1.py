from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        date = request.form['date']
        time = request.form['time']
        topic = request.form['topic']
        notes = request.form['notes']

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO sessions (name, student_id, date, time, topic, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, student_id, date, time, topic, notes))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('book.html')

if __name__ == "__main__":
    app.run(debug=True)
