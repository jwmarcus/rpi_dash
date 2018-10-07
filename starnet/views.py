# We're doing a lot of work in here. We import important flask
# components, import the app itself to set routes, set the routes
# themselves and grab models as needed to pass information
# through this business logic layer.

from starnet import app, data_handler
from starnet import sqlite_db as db

from flask import render_template, request
import sqlite3

import datetime, time

handler = data_handler.Data_Handler()

@app.route('/')
def index():
    query = "SELECT * FROM data ORDER BY date_time DESC LIMIT 1"
    rs = db.execute(query)
    payload = handler.get_data()
    return render_template('index.html', payload=payload, rs=rs[0])

@app.route('/records/', methods=['GET'])
def get_records():
    query = "SELECT * FROM data ORDER BY date_time DESC"
    rs = db.execute(query)
    return render_template('records.html', records=rs)

@app.route('/records/device/<device_key>', methods=['GET'])
def get_records_by_device_key(device_key):
    query = "SELECT * FROM data WHERE device_key IS :device_key"
    query_dict = {'device_key': device_key}
    rs = db.execute(query, query_dict)
    return render_template('records.html', records=rs)

@app.route('/records/add/', methods=['POST'])
def insert_record():
    if (request.form['device_key'] != None):
        epoch = datetime.datetime.utcfromtimestamp(0)
        t = datetime.datetime.utcnow()
        date_time_int = (t - epoch).total_seconds()

        query = "INSERT INTO data VALUES(:id, :device_key, :date_time, :field, :data)"
        query_dict = {
            'id': None,
            'device_key': request.form['device_key'],
            'date_time': int(date_time_int),
            'field': request.form['field'],
            'data': round(float(request.form['data']), 4)
        }
        db.execute(query, query_dict)
    return 'OK'

# Template Filters
@app.template_filter('datetime_format')
def datetime_format(epoch_time):
    # use dateimte.datetime.utcfromtimestamp for utc times
    # datetime.datetime.fromtimestamp automatically converst to local time
    t0 = datetime.datetime.fromtimestamp(epoch_time)
    return t0.strftime("%Y-%m-%d %H:%M:%S")
