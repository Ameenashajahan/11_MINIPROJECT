#2  model, one for item added by admin  , and another for 
#items ordered by user
from app.app import db
from app.models.usermodel import User


class Products(db.Document):
	productname =  db.StringField()
	productid = db.StringField()
	productrate = db.StringField()

class Ordereditem(db.Document):
	ordername  =  db.StringField()
	productid =db.StringField()
	productrate= db.StringField()
	orderdate  = db.StringField()
	orderedby  =  db.ReferenceField(User)
