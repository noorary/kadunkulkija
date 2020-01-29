from application import db

class Street(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
	name = db.Column(db.String(64), nullable=False)

	district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)

	def __init__(self, name):
		self.name = name
