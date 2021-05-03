# import flask

from api import app

@app.route("/")
def index_route():
    return "", 200


@app.route("/ping")
def ping_route():
    return "Alive!", 200