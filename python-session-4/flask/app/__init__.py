from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = "strong-secured-key"

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# before this add ^
bootstrap = Bootstrap(app)

# to include database models
from app import models,routes