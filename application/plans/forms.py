from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateField
from application.plans.models import Plan

class PlanForm(FlaskForm):

    street = SelectField('Street:', [validators.Length(min=5)], coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})
    date = DateField(format='%d-%m-%Y')
