from application import db
from application.models import Base

class District(Base):

    __tablename__= "district"

    name = db.Column(db.String(144), nullable=False)

    streets = db.relationship("Street", backref='district', lazy=True)

    def __init__(self, name):
      self.name = name
