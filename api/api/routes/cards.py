import flask

from api import db
from api import app
from api import tokens
from api import limiter

from ..models import Card


@app.route("/cards")
@limiter.limit("75 per minute")
def cards_route():
    cards = Card.query.all()
    
    return flask.jsonify([c.serialize() for c in cards])


@app.route("/card/<iden>", methods=["GET", "DELETE", "PUT"])
@limiter.limit("75 per minute")
def card_route(iden: int):
    req = flask.request
    card = Card.query.get_or_404(iden)
    
    if req.method == "GET":
        return flask.jsonify(card.serialize())
    elif req.method == "PUT":
        if req.headers.get("X-API-TOKEN") in tokens:
            card.update({
                "name": req.form.get("name"),
                "image": req.form.get("image"),
                "title": req.form.get("title"),
                "rarity": req.form.get("rarity"),
                "color": req.form.get("color"),
                "shiny": req.form.get("shiny") == "True",
                "description": req.form.get("description"),
            })

            db.session.commit()

            return flask.jsonify(card.serialize())
        else:
            return flask.abort(404)
    elif req.method == "DELETE":
        if req.headers.get("X-API-TOKEN") in tokens:
            db.session.delete(card)
            db.session.commit()

            return "", 204
        else:
            return flask.abort(403)


@app.route("/card/add", methods=["POST"])
@limiter.limit("10 per minute")
def card_add_route():    
    req = flask.request

    if req.headers.get("X-API-TOKEN") in tokens:
        card = Card()
        card.update({
            "name": req.form.get("name"),
            "image": req.form.get("image"),
            "title": req.form.get("title"),
            "rarity": req.form.get("rarity"),
            "color": req.form.get("color"),
            "shiny": req.form.get("shiny") == "True",
            "description": req.form.get("description")
        })

        db.session.add(card)
        db.session.commit()

        return "", 201
    else:
        return flask.abort(403)
