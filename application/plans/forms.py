from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateField
from application.plans.models import Plan

class PlanForm(FlaskForm):

    # valitse katu suoraan listasta tai rajaa kaupunginosan kadut

    street = StringField()
    date = DateField(format='%d-%m-%Y')