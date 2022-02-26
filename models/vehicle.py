#vehicle details
from app.app import db

class Vehicle(db.Document):
	name  =  db.StringField()
	number  =  db.StringField()
	district =  db.StringField()
	village  =  db.StringField()
	ward  =  db.StringField()
	timeofarrival = db.StringField(required=True)
	dateofarrival = db.StringField()
