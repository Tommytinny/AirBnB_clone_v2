#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    display state list html
    """
    states = storage.all(State)  
    return render_template('7-states_list.html', states=state.values())

@app.teardown_appcontext
def close_storage(exception):
    """
    Function to be called when the application context is torn down.
    Closes the SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
