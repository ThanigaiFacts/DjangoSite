from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect,render
import ShareMarket as shares

# Create your views here.
# -- Admin Part Starts -- #

# Admin Home page #

def admin_page(request):
    return HttpResponseRedirect(reverse('admin_home'))


#@app.route("/admin/home")
#@admin.login_required
def admin_home(request):
    return render(request,"Admin/admin.html")

'''
# Admin Login Page #
#@app.route("/admin/login", methods=['POST', 'GET'])
def admin_login_page():
    redirectPage,LoginMsg,showAlert = admin.proceedLogin()
    if redirectPage == "LoginSuccess":
        return redirect(url_for("admin_home"))
    else:
        return render_template(redirectPage,LoginStatus = LoginMsg,show_alert = showAlert)


#@app.route("/admin/logout")
def admin_logout():
    #redirectPage,LoginMsg = admin.logOut()
    redirectPage = admin.logOut()
    return redirect(redirectPage)
    #return render_template(redirectPage,LoginStatus = LoginMsg)

'''
# -- Admin Share Market Part starts -- #

#  Stock Average Calculator Page #
#@app.route("/admin/avg", methods=['POST', 'GET'])
#@admin.login_required
def stockAvgCalculator(request):
    isFieldEmpty,Text,FBQ,FBP,SBQ,SBP = shares.CalculateAveragePrice(request)
    parm = {
        "Fempty" :isFieldEmpty,
        "outText":Text,
        "FBQty"  :FBQ,
        "FBPirce":FBP,
        "SBQty"  :SBQ,
        "SBPrice":SBP
    }
    return render(request,"Admin/AvgCalculator.html",parm)
    #return render_template("Admin/AvgCalculator.html", Fempty=isFieldEmpty, outText=Text,FBQty = FBQ,FBPirce = FBP,SBQty = SBQ,SBPrice = SBP)


#  Stock Investing Page #
#@app.route("/admin/sm", methods=['POST', 'GET'])
#@admin.login_required
def stockInvest(request):
    company = shares.getCompanyList()
    isFieldsEmpty, Text,showAlert = shares.ShareMarketData(request)
    param = {
        "Fempty" : isFieldsEmpty,
        "outText" : Text,
        "show_alert" : showAlert,
        "Companies" : company
    }
    return render(request,"Admin/ShareMarket.html",param)
    #return render_template("Admin/ShareMarket.html", Fempty=isFieldsEmpty,outText=Text,show_alert = showAlert ,Companies=company)


# -- Share Market Page Ends --#

# -- Admin Part Ends -- #
