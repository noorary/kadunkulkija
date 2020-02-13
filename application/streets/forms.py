from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.districts.models import District
from application.streets.models import Street

class StreetForm(FlaskForm):
	name = StringField("Street name", [validators.DataRequired(), validators.Length(min=5, max=40, message="Invalid input")])

	district = SelectField('District:', coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})

	class Meta:
	    csrf = False

class EditStreetForm(FlaskForm):
	newname = StringField("New streetname")

	class Meta:
		csrf: False
		