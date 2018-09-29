from flask import Flask
import os
import sqlite3

app = Flask(__name__)

if not os.path.isfile("starnet-data.db"):
    conn = sqlite3.connect("starnet-data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_key text,
        date_time text,
        field text,
        data real
        )"""
    )
    conn.commit()
    conn.close()

# Circular import, chill out, it's ok.
# This is here to make sure everything in the views.py is here
# if we need it. Here for more:
# http://flask.pocoo.org/docs/1.0/patterns/packages/
import starnet.views

if __name__ == "__main__":
    app.run(host='0.0.0.0')
