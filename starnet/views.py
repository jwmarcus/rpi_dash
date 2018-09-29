# We're doing a lot of work in here. We import important flask
# components, import the app itself to set routes, set the routes
# themselves and grab models as needed to pass information
# through this business logic layer.

from flask import render_template, request
from starnet import app, data_handler
import sqlite3
import datetime

handler = data_handler.Data_Handler()

@app.route('/')
def index():
    payload = handler.get_data()
    return render_template('index.html', payload=payload)

@app.route('/records/', methods=['GET'])
def get_records():
    records = None
    return render_template('records.html', records=records)

@app.route('/records/add/', methods=['POST'])
def insert_record():
    if (request.form['device_key'] != None):
        conn = sqlite3.connect('starnet-data.db')
        c = conn.cursor()
        t = datetime.datetime.now()
        date_time_str = t.isoformat()
        c.execute("INSERT INTO data VALUES(:id, :device_key, :date_time, :field, :data)", {
            'id': None,
            'device_key': request.form['device_key'],
            'date_time': date_time_str,
            'field': request.form['field'],
            'data': round(float(request.form['data']), 4)}
        )
        conn.commit()
        c.close()
        conn.close()
    return 'OK'
