import flask
import actions

app = flask.Flask(__name__)
admins = ["frissyn", "Dart", "CoolCoderSJ"]


@app.route("/", methods=["GET", "POST"])
def index():
    req = flask.request
    name = req.headers.get("X-Replit-User-Name")

    print(name)

    if name in admins:
        if req.method == "GET":
            msg = req.args.get("msg")
            return flask.render_template("index.html", admin=True, msg=msg)
        elif req.method == "POST":
            print(req.form)
            return getattr(actions, req.form.get("action"))(req, "/")
        else:
            return flask.redirect("/")
    else:
        return flask.render_template("index.html")


@app.route("/tableview", methods=["GET", "POST"])
def table():
    req = flask.request
    name = req.headers.get("X-Replit-User-Name")

    print(name)

    if name in admins:
        if req.method == "GET":
            msg = req.args.get("msg")
            c = sorted(actions.all_cards(), key=lambda i: i["id"])
            return flask.render_template("table.html", admin=True, c=c, msg=msg)
        elif req.method == "POST":
            print(req.form)
            return getattr(actions, req.form.get("action"))(req, "/tableview")
        else:
            print(f"lol xD -> {{ {name} }}")
            return flask.redirect("/tableview")
    else:
        return flask.render_template("table.html")


app.run(host="0.0.0.0", port=8080)
