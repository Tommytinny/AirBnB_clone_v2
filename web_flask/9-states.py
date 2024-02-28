#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """
    display cities by states
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    if id == None:
        return render_template('9-states.html', states=states)
    else:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state)
            else:
                return render_template('9-states.html')

@app.teardown_appcontext
def close_storage(exception=None):
    """
    Function to be called when the application context is torn down.
    Closes the SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
