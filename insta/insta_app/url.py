from django.contrib import admin
from django.urls import path
from insta_app import views
urlpatterns = [
    path("",views.index,name='home'),
    path("login",views.loginUser,name='login'),
    path("signup",views.signUser,name='signup'),
    path("logout",views.logoutUser,name='logout'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
]
