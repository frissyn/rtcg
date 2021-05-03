import json
import flask

from api import db
from api import app
from api import tokens

from ..models import Card


@app.route("/cards")
def cards_route():
    cards = Card.query.all()
    
    return flask.jsonify([c.serialize() for c in cards])


@app.route("/card/<iden>", methods=["GET", "DELETE"])
def card_route(iden: int):
    req = flask.request
    card = Card.query.get_or_404(iden)
    
    if req.method == "GET":
        return flask.jsonify(card.serialize())
    elif req.method == "DELETE":
        db.session.delete(card)
        db.session.commit()

        return "", 204


@app.route("/card/add", methods=["POST"])
def card_add_route():    
    req = flask.request

    if req.headers.get("X-API-TOKEN") in tokens:
        card = Card()
        card.name = req.form.get("name")
        card.image = req.form.get("image")
        card.title = req.form.get("title")
        card.rarity = req.form.get("rarity")
        card.color = req.form.get("color")
        card.shiny = bool(int(req.form.get("shiny")))
        card.description = req.form.get("description")

        db.session.add(card)
        db.session.commit()

        return "", 201
    else:
        return flask.abort(403)