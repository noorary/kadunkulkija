from application import db
from application.models import Base
from application.auth.models import User
from datetime import datetime
from sqlalchemy.sql import text

street_plan = db.Table('street_plan', db.Column('street_id', db.Integer, db.ForeignKey('street.id')), 
                                      db.Column('plan_id', db.Integer, db.ForeignKey('plan.id')))

class Plan(Base):

    plandate = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    street_plans = db.relationship('Street', secondary=street_plan, backref='plan', cascade="all, delete-orphan")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


def streets_in_plan(plan_id):
    stmt = text("SELECT s.id, s.name FROM Street s"
                " JOIN street_plan sp ON sp.street_id = s.id "
                " WHERE (sp.plan_id = :plan_id)"
                ).params(plan_id=plan_id)
    
    result = db.engine.execute(stmt)

    response = []

    for row in result:
        response.append({"id":row[0], "name":row[1]})

    return response



		