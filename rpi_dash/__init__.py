from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/iotdata"
mongo = PyMongo(app)

# Circular import, chill out, it's ok.
# This is here to make sure everything in the views.py is here
# if we need it. Here for more:
# http://flask.pocoo.org/docs/1.0/patterns/packages/
import rpi_dash.views
