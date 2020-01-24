from flask_wtf import FlaskForm
from wtforms import StringField

class StreetForm(FlaskForm):
	name = StringField("Street name")

	class Meta:
	    csrf = False
