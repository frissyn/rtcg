import os
import flask
import requests
import urllib.parse


base = "https://api.rtcg.repl.co"

def all_cards():
    return requests.get(f"{base}/cards").json()

def add(req, temp: str):
    r = requests.post(
        base + "/card/add",
        headers={"X-API-TOKEN": os.getenv("TOKEN")},
        data={
            "name": req.form.get("name", ""),
            "color": req.form.get("color", ""),
            "image": req.form.get("image", ""),
            "title": req.form.get("title", ""),
            "rarity": req.form.get("rarity", ""),
            "description": req.form.get("description", ""),
            "shiny": req.form.get("shiny") == "True",
        }
    )

    if r.status_code <= 399: msg = "Card added successfully."
    else: msg = f"An error occured: {r.content}"

    return flask.redirect(f"{temp}?msg={urllib.parse.quote(msg, safe='~()*!.')}")

def delete(req, temp: str):
    r = requests.delete(
        base + "/card/" + req.form.get("id"),
        headers={"X-API-TOKEN": os.getenv("TOKEN")}
    )

    if r.status_code <= 399: msg = "Card deleted successfully."
    else: msg = f"An error occured: {r.content}"

    return flask.redirect(f"{temp}?msg={urllib.parse.quote(msg, safe='~()*!.')}")

def update(req, temp: str):
    r = requests.put(
        base + "/card/" + req.form.get("id"),
        headers={"X-API-TOKEN": os.getenv("TOKEN")},
        data={
            "name": req.form.get("name", ""),
            "color": req.form.get("color", ""),
            "image": req.form.get("image", ""),
            "title": req.form.get("title", ""),
            "rarity": req.form.get("rarity", ""),
            "description": req.form.get("description", ""),
            "shiny": req.form.get("shiny") == "True",
        }
    )

    if r.status_code <= 399: msg = "Card updated successfully."
    else: msg = f"An error occured: {r.content}"

    return flask.redirect(f"{temp}?msg={urllib.parse.quote(msg, safe='~()*!.')}")
