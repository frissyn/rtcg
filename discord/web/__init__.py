import flask
import threading

app = flask.Flask(__name__)

@app.route("/")
def index(): return ""

@app.route("/ping")
def ping(): return "pong"

server = threading.Thread(
    target=app.run,
    kwargs={
        "host": "0.0.0.0",
        "port": 8080,
        "debug": False,
        "threaded": True
    }
)
