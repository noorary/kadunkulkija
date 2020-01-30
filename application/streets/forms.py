from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.districts.models import District
from application.streets.models import Street

class StreetForm(FlaskForm):
	name = StringField("Street name", [validators.Length(min=5)])
	districts_database = District.query.with_entities(District.id, District.name)
	districts_field = [(x.id, x.name) for x in districts_database]

	district = SelectField("District", choices=districts_field, coerce=int)

	class Meta:
	    csrf = False

class EditStreetForm(FlaskForm):
	newname = StringField("New streetname")

	class Meta:
		csrf: False