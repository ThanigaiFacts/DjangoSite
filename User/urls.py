from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('Projects/Game', views.NumberGuessing_fun, name='guessingGame'),
    path('Projects/News/<int:num>', views.newsFun, name='news'),
    path('BlogIndex', views.blogIndexFun, name='blogIndex'),
    path('DetailBlog/<int:num>', views.DetailBlog, name='detailblog'),
    path('contact', views.contact, name='contact')
]
