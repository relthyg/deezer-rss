from flask import Flask
from flask_caching import Cache

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
cache = Cache(app)

from app import routes
