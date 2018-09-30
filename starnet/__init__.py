from starnet.sqlite_db import Sqlite_DB

from flask import Flask
import sqlite3

import os

app = Flask(__name__)
sqlite_db = Sqlite_DB('starnet-data.db')

# Circular import, chill out, it's ok.
# http://flask.pocoo.org/docs/1.0/patterns/packages/
import starnet.views

if __name__ == "__main__":
    app.run(host='0.0.0.0')
