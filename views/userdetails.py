#for user signup
import json
from datetime import datetime
from app.app import login_manager
from app.models.usermodel import User,UserSell,UserPurchase
from app.models.vehicle import Vehicle

from flask_restful import Resource
# from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

#user login
def userlogin():
	#user login
	if request.method == 'POST':
		user = User.objects.get(usermailid=request.form["usermailid"])
		if(user.userpassword==request.form["password"]):
			login_user(user)
			# flash('You were successfully logged in')
			# return redirect(url_for('orderitem'))
			vehicle=Vehicle.objects()
			return render_template("userview.html")
		else:
			render_template('login.html')
	return render_template('login.html')
#to view user cart
def usercart():
	user = User.objects.get(username=current_user.username)
	return render_template('card.html',user=user)


#usersell
def usersell():
	if request.method =='POST':
		now = datetime.utcnow()
		plasticdetails = {"Polystyrene":10,
		"Polypropylene":5,
		"LowDensityPolythene":15,
		"PVC":20,
		"HighDensityPolythene":10,
		"polyester":20}
		username  = current_user.username
		weight = request.form["weight"]
		plastictype = request.form["type"]
		district = request.form["district"]
		village = request.form["village"]
		ward = request.form["ward"]
		coins  = int(weight) * plasticdetails[plastictype]
		date_time = now.strftime("%m/%d/%Y %H:%M:%S") 
		UserSell.objects.create(datetime=date_time,username=username,ward=ward,village=village,
			district=district,plastictype=plastictype,plastictwt=weight,coins=coins)
		user = User.objects.get(username=username)
		user.usercoin = user.usercoin+ coins
		user.save()
		flash('Your order is successfully completed', 'success')
		return render_template("userview.html")

@login_required
def vehicleview():
	vehicle=Vehicle.objects()
	return  render_template("vehicleuser.html",vehicles=vehicle)

@login_required
def useristory():
	if (current_user.userrole =="admin"):
		print(12345)
		history  =  UserSell.objects()
	else:
		history  =  UserSell.objects(username = current_user.username)
	print(history)
	return render_template("userhistory.html",history=history)
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
@login_required
def logout():
	logout_user()
	return redirect(url_for('userlogin'))

@login_required
def productpurchase():
	if request.method =='POST':
		dict1 = request.form
		key, value = list(dict1.items())[0]
		cost = value
		productname =  key
		username  = current_user.username
		user = User.objects.get(username=username)
		user.usercoin = user.usercoin-int(cost)
		if (user.usercoin<0):
			flash('You dont have enough coins', 'error')
		else:
			user.save()
			now = datetime.utcnow()
		# coins  = int(weight) * plasticdetails[plastictype]
			date_time = now.strftime("%m/%d/%Y %H:%M:%S")
			UserPurchase.objects.create(datetime=date_time,username=username,
				cost=cost,productname=productname)
			flash('You have successfully purchased', 'success')
		return render_template("purchase.html")
	else:
		return render_template("purchase.html")
@login_required
def purchaseHistory():
	if (current_user.userrole =="admin"):
		print(12345)
		history  =  UserPurchase.objects()
	else:
		history  =  UserPurchase.objects(username = current_user.username)
	return render_template("purchasehistory.html",history=history)

@login_required
def userProfile():
	user = User.objects.get(username=current_user.username)
	return render_template('userprofile.html',user=user)