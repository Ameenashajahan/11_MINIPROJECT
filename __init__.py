#routers
from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.userdetails import userlogin,userProfile,productpurchase,userregister,logout,usercart,usersell,vehicleview,useristory,purchaseHistory
from app.views.admin import adminLogin,userview,vehicleManegement
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
#for login
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
# #for user register
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])
#admin user
app.add_url_rule("/admin",view_func=adminLogin,methods=["GET","POST"])
#logout
app.add_url_rule("/logout",view_func=logout,methods=["GET"])
#admin userview
app.add_url_rule("/adminuser",view_func=userview)
#vehicle registration
app.add_url_rule("/vehicleUser",view_func=vehicleManegement,methods=["GET","POST"])
#usercart
app.add_url_rule("/usercart",view_func=usercart)
#user selling
app.add_url_rule("/usersell",view_func=usersell,methods=["GET","POST"])
#user vehicle view
app.add_url_rule("/vehicleview",view_func=vehicleview)
#user selling history
app.add_url_rule("/useristory",view_func=useristory)
#purchasing
app.add_url_rule("/purchase",view_func=productpurchase,methods=["GET","POST"])
#purchase history
app.add_url_rule("/purchaseHistory",view_func=purchaseHistory,methods=["GET","POST"])
#userprofile
app.add_url_rule("/userprofile",view_func=userProfile,methods=["GET","POST"])