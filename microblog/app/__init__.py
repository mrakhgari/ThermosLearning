from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
## for read config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models need for database
from app import routes, models
