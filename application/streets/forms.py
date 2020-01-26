from flask_wtf import FlaskForm
from wtforms import StringField, validators

class StreetForm(FlaskForm):
	name = StringField("Street name", [validators.Length(min=5)])

	class Meta:
	    csrf = False
