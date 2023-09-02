"""Module providing random choices."""
from random import choices
from flask import render_template
from flask import Flask



app = Flask(__name__)


def random_fruit():
    """Returns random fruit"""

    fruits = ["apple", "cherry", "orange", "banana", "pawpaw", "grapes"]
    return choices(fruits)


@app.route("/")
def fruit():
    """Return random fruit"""

    my_fruit = random_fruit()
    return render_template("index.html", title="Random Fruit", fruit=my_fruit)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
