from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from adminControl import AdminControl
import ShareMarket as shares

# Create your views here.
# -- Admin Part Starts -- #

admin = AdminControl()


# Admin Home page #

def admin_page(request):
    return HttpResponseRedirect(reverse('admin_home'))


@admin.login_required
def admin_home(request):
    return render(request, "Admin/admin.html")


# Admin Login Page #

def admin_login_page(request):
    redirectPage, LoginMsg, showAlert = admin.proceedLogin(request)
    if redirectPage == "LoginSuccess":
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        param = {
            "LoginStatus": LoginMsg,
            "show_alert": showAlert
        }
        return render(request, redirectPage, param)


def admin_logout(request):
    redirectPage = admin.logOut()
    return HttpResponseRedirect(redirectPage)


# -- Admin Share Market Part starts -- #


#  Stock Average Calculator Page #

@admin.login_required
def stockAvgCalculator(request):
    isFieldEmpty, Text, FBQ, FBP, SBQ, SBP = shares.CalculateAveragePrice(request)
    parm = {
        "Fempty": isFieldEmpty,
        "outText": Text,
        "FBQty": FBQ,
        "FBPirce": FBP,
        "SBQty": SBQ,
        "SBPrice": SBP
    }
    return render(request, "Admin/AvgCalculator.html", parm)


#  Stock Investing Page #

@admin.login_required
def stockInvest(request):
    company = shares.getCompanyList()
    isFieldsEmpty, Text, showAlert = shares.ShareMarketData(request)
    param = {
        "Fempty": isFieldsEmpty,
        "outText": Text,
        "show_alert": showAlert,
        "Companies": company
    }
    return render(request, "Admin/ShareMarket.html", param)

# -- Share Market Page Ends --#

# -- Admin Part Ends -- #
