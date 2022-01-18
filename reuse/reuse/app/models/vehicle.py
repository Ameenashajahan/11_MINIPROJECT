#vehicle details
from app.app import db

class Vehicle(db.Document):
	name  =  db.StringField()
	number  =  db.StringField()
	location = db.StringField(required=True)
	pinno = db.StringField(required=True,unique=True)
	dayofarrival = db.StringField(required=True)
	timeofarrival = db.StringField(required=True)
	dataofarrival = db.StringField()
