#for user signup
import json
from app.app import login_manager
from app.models.usermodel import User
from flask_restful import Resource
# from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user
def userlogin():
	#user login
	if request.method == 'POST':
		user = User.objects.get(usermailid=request.form["usermailid"])
		if(user.userpassword==request.form["password"]):
			login_user(user)
			flash('You were successfully logged in')
			# return redirect(url_for('orderitem'))
			return "successfully  logged in"
		else:
			render_template('login.html')
	return render_template('login.html')

def userregister():
	#user registerd
	if request.method == 'POST':
		name  = request.form["name"]
		username = request.form["username"]
		userpasswords = request.form["password"]
		usermailid = request.form["usermailid"]
		# userrole = request.form["userrole"]
		deliveryaddress = request.form["deliveryaddress"]
		pinno =  request.form["pinno"]
		deliveryaddresslist = []
		deliveryaddresslist.append(deliveryaddress)
		userphoneno = request.form["userphoneno"]
		print(request.form)
		User.objects.create(name=name,username=username,userpassword=userpasswords,
			usermailid=usermailid,pinno=pinno,
			deliveryaddress=deliveryaddresslist,userphoneno=userphoneno)
		return redirect(url_for('userlogin'))
	else:
		return render_template('register.html')
def logout():
	logout_user()
	return redirect(url_for('userlogin'))
