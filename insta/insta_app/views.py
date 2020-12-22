from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index(request):
    return HttpResponse("hello bruh")
# creating login userr
def loginUser(request):
    if request == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            render(request,'login.html')
    return render(request,'login.html')
def logoutUser(request):
    return HttpResponse("hello up")
def signUser(request):
    return HttpResponse("hello he")