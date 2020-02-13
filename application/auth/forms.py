from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username",[validators.DataRequired(message="username can't be empty"), validators.Length(min=3, max=30, message="Username must be between 3 to 30 characters")])
    password = PasswordField("Password" , [validators.DataRequired(message="password can't be empty"), validators.Length(min=8, message="password must contain at least 8 characters")])

    class Meta:
      csrf = False
