from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DistrictForm(FlaskForm):
	name = StringField("District name", [validators.Length(min=5, max=25, message="District name is too short or too long")])

	class Meta:
	    csrf = False
