#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    display cities by states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def close_storage(exception=None):
    """
    Function to be called when the application context is torn down.
    Closes the SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
