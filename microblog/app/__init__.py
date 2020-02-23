from flask import Flask
from config import Config


app = Flask(__name__)
## for read config
app.config.from_object(Config)
from app import routes
