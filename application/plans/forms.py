from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SelectMultipleField, DateField
from application.plans.models import Plan
from datetime import date

class PlanForm(FlaskForm):

    street = SelectField('Street:', coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})
    plandate = DateField(format='%d.%m.%Y', default=date.today)

class MoreStreets(FlaskForm):

    street = SelectField('STreet:', coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})