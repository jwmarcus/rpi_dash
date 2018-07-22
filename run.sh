#!/bin/bash

export FLASK_APP=rpi_dash:app
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=5655
