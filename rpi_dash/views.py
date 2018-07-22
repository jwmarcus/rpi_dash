# We're doing a lot of work in here. We import important flask
# components, import the app itself to set routes, set the routes
# themselves and grab models as needed to pass information
# through this business logic layer.

from flask import render_template
from rpi_dash import app

@app.route('/')
def hello_world():
    return "Hello, World! I'm alive!"

@app.route("/template/")
@app.route("/template/<name>") # catches sub-route, sets vars
def template(name=None):
    return render_template('index.html', name=name)
