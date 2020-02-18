from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DistrictForm(FlaskForm):
	name = StringField("District name", [validators.Length(min=5, max=25, message="District name should be between 5 and 25 characters.")])

	class Meta:
	    csrf = False
