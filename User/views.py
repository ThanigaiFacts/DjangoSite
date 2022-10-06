from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect,render

# Create your views here.


# --- User Part Starts --- #

# Home page Routing #
def index(request):
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request, "User\index.html")

# Contact page Routing #
def contact():
    #msgSentStatus, msgStatus = admin.contact_admin()
    #return render("User/contact.html", msg=msgStatus, msgSent=msgSentStatus)
    render("User/contact.html")


# Guessing Game page Routing #
def NumberGuessing_fun():
    #variable.generateRandomNumber()
    #return render("User/GuessingNumber.html", number=variable.randomNum)
    render("User/GuessingNumber.html")


# Blog page Routing #
def blogIndexFun():
    #variable.blogResp = variable.utilityObj.getBlogData()
    #return render("User/blogindex.html", jobj=variable.blogResp)
    render("User/blogindex.html")


def showDetailBlog(num):
    #return render("User/blog.html", jobj=variable.blogResp, blogNum=num - 1)
    render("User/blog.html")


# News page Routing #
def newsFun(num):
   # news.loadNews(num)
    #return render_template("User/news.html", newsData=news.NewsHeader, newsImg=news.NewsImg, newsLink=news.NewsLink,
                          # detailedNews=news.detailNews, pageCounter=news.URlNextPage, posCounter=news.counterPos,
                          # newsDt=news.Date)
   return render("User/news.html")

# -- User Part Ends -- #
