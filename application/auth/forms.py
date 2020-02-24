from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    username = StringField("Username",[validators.DataRequired(message="username can't be empty"), validators.Length(min=3, max=30, message="Username must be between 3 to 30 characters")])
    password = PasswordField("Password" , [validators.DataRequired(message="password can't be empty"), validators.Length(min=8, max =50, message="password must be between 8 to 50 characters")])

    class Meta:
      csrf = False
