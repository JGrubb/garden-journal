from flask import Flask
from flask import request
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def show_list():
    return "hello world"

@app.route('/new', methods=['POST'])
def add_new_entry():
    if request.method == 'POST':
        data = request.get_json(force=True)
        insert_sql = 'INSERT INTO entries (timestamp, key, value) VALUES (?, ?, ?)'
        conn = sqlite3.connect('data/data.db')
        c = conn.cursor()
        c.execute(insert_sql, (datetime.now(), data['key'], data['value']))
        conn.commit()
        return data