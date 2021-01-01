from django.contrib import admin
from django.urls import path
from insta_app import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path("",views.index,name='home'),
    path("login",views.loginUser,name='login'),
    path("signup",views.signUser,name='signup'),
    path("logout",views.logoutUser,name='logout'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("new",views.new,name='new'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
