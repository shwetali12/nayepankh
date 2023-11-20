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
    path('logout/',views.logoutpage,name='logout'),
    path('feedback/',views.feedback,name='feedback'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('community/',views.community,name='community'),
    path('post_detail/<int:id>/',views.post_detail,name='post_detail'),
    path('post_detail/<int:id>/comment/',views.comment, name='comment'),
    path('create_post/',views.create_post,name='create_post'),







   
]