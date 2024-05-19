#!/usr/bin/python3
"""Import Flask to run the web"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Renders state_list html page to display States created"""
    states = storage.all()
    return render_template('7-states_lists.html', states=states)


@app.teardown_appconteext
def teardown(self):
    """Method that removes current SQLAlchemy Session"""
    storaage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
