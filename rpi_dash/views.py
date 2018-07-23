# We're doing a lot of work in here. We import important flask
# components, import the app itself to set routes, set the routes
# themselves and grab models as needed to pass information
# through this business logic layer.

from flask import render_template
from rpi_dash import app
# TODO: this feels dirty, not sure why
from rpi_dash.data_handler import Data_Handler

handler = Data_Handler()

@app.route('/')
def index():
    payload = handler.get_data()
    return render_template('index.html', payload=payload)
