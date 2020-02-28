from application import db
from application.models import Base
from application.auth.models import User
from datetime import datetime
from sqlalchemy.sql import text

street_plan = db.Table('street_plan', db.Column('street_id', db.Integer, db.ForeignKey('street.id')), 
                                      db.Column('plan_id', db.Integer, db.ForeignKey('plan.id')), 
                                      db.PrimaryKeyConstraint('street_id', 'plan_id'))

class Plan(Base):

    plandate = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    street_plans = db.relationship('Street', secondary=street_plan, backref='plan')
    # street_id = db.Column(db.Integer, db.ForeignKey('street.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


def streets_in_plan(plan_id):
    stmt = text("SELECT Street.id, Street.name FROM Street"
                " LEFT JOIN street_plan ON street_plan.plan_id = :plan_id "
                " WHERE (street_plan.plan_id = :plan_id)"
                " GROUP BY Street.name "
                ).params(plan_id=plan_id)
    
    result = db.engine.execute(stmt)

    response = []

    for row in result:
        response.append({"id":row[0], "name":row[1]})

    return response



		