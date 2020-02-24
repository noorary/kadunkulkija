from application import db
from application.models import Base
from application.auth.models import User
from datetime import datetime

class Plan(Base):

    plandate = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

		


		