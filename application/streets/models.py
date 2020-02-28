from application import db
from application.models import Base
from application.plans.models import Plan, street_plan

from sqlalchemy.sql import text

class Street(Base):

	__tablename__="street"

	name = db.Column(db.String(64), nullable=False)

	district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
	street_plans = db.relationship('Plan', secondary=street_plan, backref='street')

	def __init__(self, name): 
		self.name = name

		
	def users_plan(account_id):

		stmnt = text("SELECT plan.id, plan.plandate, plan.completed FROM plan"
					" JOIN account ON account.id = account_id"
					" WHERE account.id = plan.account_id")

		result = db.engine.execute(stmnt)

		response = []

		for row in result:
			response.append({"id":row[0], "plandate":row[1], "completed":row[2]})

	@staticmethod
	def find_streets_in_many_plans():
		stmt=text("SELECT Street.id, Street.name FROM Street"
		" LEFT JOIN street_plan ON street_plan.street_id = Street.id"
		" GROUP BY Street.id"
		" HAVING COUNT(street_plan.plan_id) >= 1")

		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"id":row[0], "name":row[1]})

		return response