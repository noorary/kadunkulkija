from flask import Flask
from flask_migrate import Migrate
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///streets.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#login functionality

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login"

# roles in login_required
from functools import wraps
from flask_login import current_user

from application import views

from application.districts import models
from application.streets import models
from application.plans import models

from application.streets import views
from application.districts import views
from application.plans import views
from application.stats import views

from application.auth import models
from application.auth import views

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    db.session.commit()

except:
    pass


