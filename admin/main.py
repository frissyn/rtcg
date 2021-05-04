import os
import flask
import requests

app = flask.Flask(__name__)
admins = ["frissyn", "Dart"]
base = "https://api.rtcg.repl.co"


@app.route("/", methods=["GET", "POST"])
def index():
    req = flask.request
    name = req.headers.get("X-Replit-User-Name")

    if name in admins:
        if req.method == "GET":
            return flask.render_template("index.html", admin=True)
        else:
            if req.form.get("action") == "add":
                req = flask.request
                h = {"X-API-TOKEN": os.getenv("TOKEN")}
                p = {
                    "name": req.form.get("name"),
                    "color": req.form.get("color"),
                    "image": req.form.get("image"),
                    "title": req.form.get("title"),
                    "rarity": req.form.get("rarity"),
                    "description": req.form.get("description"),
                    "shiny": "1" if req.form.get("shiny") else "0",
                }

                res = requests.post(base + "/card/add", headers=h, data=p)

                print(res.status_code)
                print(res.content)

                return flask.render_template("index.html", admin=True, msg="Card Added.")
            elif req.form.get("action") == "delete":
                i = req.form.get("id")
                h = {"X-API-TOKEN": os.getenv("TOKEN")}

                res = requests.delete(base + f"/card/{i}", headers=h)

                print(res.status_code)
                print(res.content)

                return flask.render_template("index.html", admin=True, msg="Card Deleted.")
            else:
                return flask.redirect("/")
    else:
        return flask.render_template("index.html")


app.run(host="0.0.0.0", port=8080)
