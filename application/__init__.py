from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///streets.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import views

from application.streets import models
from application.streets import views

db.create_all()


