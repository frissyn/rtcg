import flask
import actions

app = flask.Flask(__name__)
admins = ["frissyn", "Dart"]


@app.route("/", methods=["GET", "POST"])
def index():
    req = flask.request
    name = req.headers.get("X-Replit-User-Name")

    if name in admins:
        if req.method == "GET":
            return flask.render_template("index.html", admin=True)
        elif req.method == "POST":
            return getattr(actions, req.form.get("action"))(req)
        else:
            return flask.redirect("/")
    else:
        return flask.render_template("index.html")


app.run(host="0.0.0.0", port=8080)