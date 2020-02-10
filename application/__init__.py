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

from application import views

from application.districts import models
from application.streets import models
from application.plans import models

from application.streets import views
from application.districts import views
from application.plans import views

from application.auth import models
from application.auth import views


from application.auth.models import User

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login"

from functools import wraps

# def login_required(_func=None, *, role="ANY"):
#     def wrapper(func):
#         @wraps(func)
#         def decorated_view(*args, **kwargs):
#             if not (current_user and current_user.is_authenticated):
#                 return login_manager.unauthorized()

#             acceptable_roles = set(("ANY", *current_user.roles()))

#             if role not in acceptable_roles:
#                 return login_manager.unauthorized()

#             return func(*args, **kwargs)
#         return decorated_view
#     return wrapper if _func is None else wrapper(_func)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    db.create_all()
    db.session.commit()

except:
    pass


