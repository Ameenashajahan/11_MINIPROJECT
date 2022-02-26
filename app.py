#application defined here 
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_restful import  Api
from flask_login import current_user
login_manager = LoginManager()
app = Flask(__name__, static_folder='../frontend/static',
            template_folder='../frontend/templates', instance_relative_config=True)
app.config["MONGODB_SETTINGS"] = {
	"db":"reuse",
	"host":"localhost",
	"port":27017
}
app.secret_key = b'_5#y2L"Fjnmb\n\xec]/'
db =  MongoEngine(app)
api = Api(app)
