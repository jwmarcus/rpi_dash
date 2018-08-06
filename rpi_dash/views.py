# We're doing a lot of work in here. We import important flask
# components, import the app itself to set routes, set the routes
# themselves and grab models as needed to pass information
# through this business logic layer.

from flask import render_template, request
from rpi_dash import app, data_handler, mongo

handler = data_handler.Data_Handler()

@app.route('/')
def index():
    payload = handler.get_data()
    return render_template('index.html', payload=payload)

@app.route('/records/')
def get_documents():
    records = mongo.db.measurements.find({})
    return render_template('records.html', records=records)

@app.route('/records/add/', methods=['POST'])
def insert_document():
    new_doc = request.form['number']
    print(new_doc)
    return render_template('base.html')
    # number = request.form['']
