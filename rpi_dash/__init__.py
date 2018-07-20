from flask import Flask

app = Flask(__name__)

import rpi_dash.views

# Circular import, chill out, it's ok.
# This is here to make sure everything in the views.py is here
# if we need it. Here for more:
# http://flask.pocoo.org/docs/1.0/patterns/packages/
