from application import db
from application.models import Base 

from sqlalchemy.sql import text
import os

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    admin = db.Column(db.Boolean, default=False, nullable=False)

    plans = db.relationship("Plan", backref='account', lazy=True)
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    # def roles(self):
    #     return ["ADMIN", "USER"]

    @staticmethod
    def find_users_with_fiveormore_completed():

        if os.environ.get("HEROKU"):

            stmt = text("SELECT Account.id, Account.name FROM Account"
                        " LEFT JOIN Plan ON Plan.account_id = Account.id"
                        " WHERE (Plan.completed = 'true')"
                        " GROUP BY Account.id"
                        " HAVING COUNT(Plan.id) >= 5")
        else: 

            stmt = text("SELECT Account.id, Account.name FROM Account"
                        " LEFT JOIN Plan ON Plan.account_id = Account.id"
                        " WHERE (Plan.completed = 1)"
                        " GROUP BY Account.id"
                        " HAVING COUNT(Plan.id) >= 5")
                        
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response