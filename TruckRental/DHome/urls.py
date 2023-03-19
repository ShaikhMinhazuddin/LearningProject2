from django.urls import path
from . import views

urlpatterns = [
    path('',views.chome,name ='chome'),
    path('cform',views.cform, name = 'cform'),
    path('rhome',views.rhome, name = 'rhome'),
    path('loginuser',views.loginuser, name = 'loginuser'),
    path('register', views.register, name = 'register'),
    path('dhome', views.dhome, name = 'dhome'),
    path('logoutuser', views.logoutuser , name = 'logoutuser')
]