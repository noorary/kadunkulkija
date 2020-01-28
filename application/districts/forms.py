from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DistrictForm(FlaskForm):
	name = StringField("District name", [validators.Length(min=5)])

	class Meta:
	    csrf = False
