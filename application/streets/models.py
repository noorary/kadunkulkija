from application import db
from application.models import Base

from sqlalchemy.sql import text

class Street(Base):

	__tablename__="street"

	name = db.Column(db.String(64), nullable=False)

	district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)

	plans = db.relationship("Plan", backref='street', lazy=True)	

	def __init__(self, name):
		self.name = name


	@staticmethod
	def find_streets_in_many_plans():
		stmt=text("SELECT Street.id, Street.name FROM Street"
		" LEFT JOIN Plan ON Plan.street_id = Street.id"
		" GROUP BY Street.id"
		" HAVING COUNT(Plan.id) >= 1")

		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"id":row[0], "name":row[1]})

		return response