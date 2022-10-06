from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect,render
import utility

# Create your views here.


# --- User Part Starts --- #

blogResp = None

# Home page Routing #
def index(request):
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request, "User\index.html")

# Contact page Routing #
def contact(request):
    msgSentStatus, msgStatus = utility.contact_admin(request)
    return render(request,"User/contact.html",{'msg' : msgStatus,'msgSent' : msgSentStatus})


# Guessing Game page Routing #
def NumberGuessing_fun(request):
    randomNum = utility.generateRandomNumber()
    return render(request,"User/GuessingNumber.html",{"number" : randomNum})


# Blog page Routing #
def blogIndexFun(request):
    global blogResp
    blogResp = utility.getBlogData()
    #return HttpResponse("Blog")
    return render(request,"User/blogindex.html",{'jobj' : blogResp[0]["blog"]})


def DetailBlog(request,num):
    global blogResp
    #return render("User/blog.html", jobj=variable.blogResp, blogNum=num - 1)
    return render(request,"User/blog.html",{'jobj' :  blogResp[0]["blog"][num]})


# News page Routing #
def newsFun(request,num):
   # news.loadNews(num)
    #return render_template("User/news.html", newsData=news.NewsHeader, newsImg=news.NewsImg, newsLink=news.NewsLink,
                          # detailedNews=news.detailNews, pageCounter=news.URlNextPage, posCounter=news.counterPos,
                          # newsDt=news.Date)
   return render(request,"User/news.html")

# -- User Part Ends -- #
