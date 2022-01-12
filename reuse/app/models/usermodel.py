#for user and delivery user databse
from app.app import db

class User(db.Document):
	name  =  db.StringField()
	pinno  =  db.StringField()
	username = db.StringField(required=True)
	usermailid = db.StringField(required=True,unique=True)
	userrole = db.StringField(required=True,default="normal")
	userpassword = db.StringField(required=True)
	deliveryaddress = db.ListField()
	userphoneno = db.StringField(required=True)

	def is_authenticated(self):
		return True

	def get_id(self):
		return str(self.id)

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_role(self):
		return self.role

	def check_role(self, roles):
		return self.role in roles

	# meta = {
	# 	'allow_inheritance': True,
	# 	'indexes': ['-date_created', 'email'],
	# 	'ordering': ['-date_created']
	# }
