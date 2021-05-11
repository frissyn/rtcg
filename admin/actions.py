import os
import flask
import requests

base = "https://api.rtcg.repl.co"

def add(req):
    requests.post(
        base + "/card/add",
        headers={"X-API-TOKEN": os.getenv("TOKEN")},
        data={
        "name": req.form.get("name"),
        "color": req.form.get("color"),
        "image": req.form.get("image"),
        "title": req.form.get("title"),
        "rarity": req.form.get("rarity"),
        "description": req.form.get("description"),
        "shiny": "1" if req.form.get("shiny") else "0",
    })

    return flask.render_template("index.html", admin=True, msg="Card Added.")


def delete(req):
    requests.delete(
        base + "/card/" + req.form.get("id"),
        headers={"X-API-TOKEN": os.getenv("TOKEN")}
    )

    return flask.render_template("index.html", admin=True, msg="Card Deleted.")


def update(req):
    res = requests.put(
        base + "/card/" + req.form.get("id"),
        headers={"X-API-TOKEN": os.getenv("TOKEN")},
        data={
        "name": req.form.get("name"),
        "color": req.form.get("color"),
        "image": req.form.get("image"),
        "title": req.form.get("title"),
        "rarity": req.form.get("rarity"),
        "description": req.form.get("description"),
        "shiny": "1" if req.form.get("shiny") else "0",
    })

    print(res.status_code)
    print(res.content)

    return flask.render_template("index.html", admin=True, msg="Card Updated.")