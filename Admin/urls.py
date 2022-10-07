from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_page, name='admin_page'),
    path('home', views.admin_home, name='admin_home'),
    #path('login', views.admin_login_page, name='admin_login_page'),
    #path('logout', views.admin_logout, name='admin_logout'),
    path('ShareMarket/StockAvg', views.stockAvgCalculator, name='stockAvgCalculator'),
    path('ShareMarket/Invest', views.stockInvest, name='stockInvest'),
    # path('ShareMarket/Trade', views.stockTrade, name='stockTrade')
]
