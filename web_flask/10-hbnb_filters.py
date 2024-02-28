#!/usr/bin/python3
"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import  Amenity

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    display cities by states
    """
    states = storage.all(State).values()
    city = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def close_storage(exception=None):
    """
    Function to be called when the application context is torn down.
    Closes the SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
