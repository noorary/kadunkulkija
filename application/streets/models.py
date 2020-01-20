from application import db

class Street(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(64), nullable=False)

	def __init__(self, name):
		self.name = name
