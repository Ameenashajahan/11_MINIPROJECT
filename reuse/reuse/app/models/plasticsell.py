#model for items selled by user
from app.app import db

class Plastic(db.Document):
	plastictype  =  db.StringField()
	quantity  =  db.StringField()
	rate = db.StringField(required=True)
	totalamount = db.StringField(required=True,unique=True)
	user = db.ReferenceField(User)