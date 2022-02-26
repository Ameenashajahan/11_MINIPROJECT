import json
from app.app import login_manager
from app.models.usermodel import User
from app.models.vehicle import Vehicle
from flask_restful import Resource
# from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def adminLogin():
	if request.method == 'POST':
		user = User.objects.get(usermailid=request.form["usermailid"])
		if(user.userpassword==request.form["password"] and (user.userrole=="admin")):
			login_user(user)
			flash('You were successfully logged in')
			# return redirect(url_for('orderitem'))
			users = User.objects()
			return render_template("adminpage.html")
		else:
			render_template('admin.html')
	return render_template('admin.html')

def userview():
	if(current_user.userrole=="admin"):
		users = User.objects()
		print(users)
		return render_template("userdetails.html",users = users)



def vehicleManegement():
	if(current_user.userrole=="admin"):
		if (request.method == 'POST'):
			name = request.form["name"]
			number =  request.form["number"]
			district =  request.form["district"]
			village  =  request.form["village"]
			ward  =  request.form['ward']
			# location = request.form["location"]
			# pinno = request.form["pinno"]
			dateofarrival = request.form["dateofarrival"]
			timeofarrival = request.form["timeofarrival"]
			Vehicle.objects.create(name=name,number=number,district=district,
				village=village,ward=ward,dateofarrival=dateofarrival,
				timeofarrival=timeofarrival)
			vehicle=Vehicle.objects()
			return render_template("vehicledetails.html",vehicles=vehicle)
		else:
			vehicle=Vehicle.objects()
			return render_template("vehicledetails.html",vehicles=vehicle)

