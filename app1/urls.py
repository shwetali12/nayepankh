from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('certificates/',views.certificates,name='certificates'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('donate/',views.donate,name='donate'),
    path('signuppage/',views.signuppage,name='signuppage'),
    path('loginpage/',views.loginpage,name='loginpage'),





   
]