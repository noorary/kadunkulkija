from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.districts.models import District
from application.streets.models import Street

class StreetForm(FlaskForm):
	name = StringField("Street name", [validators.DataRequired(message="Street name can't be empty"), validators.Length(min=5, max=40, message="Name must be between 5 and 40 characters")])

	district = SelectField('District:', coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})

	class Meta:
	    csrf = False

class EditStreetForm(FlaskForm):
	newname = StringField("New streetname", [validators.DataRequired(), validators.Length(min=5, max=40, message="New name must be between 5 and 40 characters")])

	class Meta:
		csrf: False
		