#!/usr/bin/python3
"""Imports Flask to run the web"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """method to close the session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays html page with states and cities"""
    states = storage.all(State)
    return render_tempplate('8-cities_by_states.html', states=states)


if __name__ == "__Main__":
    app.run(host='0.0.0.0', port="5000")
