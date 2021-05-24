import os
import flask
import secrets
import psycopg2

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = flask.Flask(__name__)
app.config.from_mapping({
    "DEBUG": False,
    "TESTING": False,
    "FLASK_DEBUG": 0,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SECRET_KEY": secrets.token_hex(16),
    "SQLALCHEMY_DATABASE_URI": os.environ["DATABASE_URL"],
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})
conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='require')
limiter = Limiter(
    app, default_limits=["75 per minute"],
    key_func=get_remote_address
)

tokens = [os.getenv("TOKEN")]
db = SQLAlchemy(app)
migrator = Migrate(app, db)

from .routes import *