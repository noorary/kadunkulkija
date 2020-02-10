from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateField
from application.plans.models import Plan

class PlanForm(FlaskForm):

    street = SelectField('Street:', coerce=int, render_kw={"class": "chosen-select", "data-placeholder":"..."})
    plandate = DateField(format="'%d-%m-%Y'")
