import os
import flask
import secrets

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config.from_mapping({
    "DEBUG": False,
    "TESTING": False,
    "FLASK_DEBUG": 0,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SECRET_KEY": secrets.token_hex(16),
    "SQLALCHEMY_DATABASE_URI": "sqlite:///db/site.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

tokens = [os.getenv("TOKEN")]
db = SQLAlchemy(app)
migrator = Migrate(app, db)

from .routes import *