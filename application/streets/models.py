from application import db
from application.models import Base

class Street(Base):

	__tablename__="street"

	name = db.Column(db.String(64), nullable=False)

	district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)

	plans = db.relationship("Plan", backref='street', lazy=True)	

	def __init__(self, name):
		self.name = name
