from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from insta_app.models import posts
from .forms import *
# Create your views here.
def index(request):
    if str(request.user) == 'AnonymousUser':
        return redirect("/login")  
    post=posts.objects.all()     
    return render(request,'index.html',{"post":post})    
# creating login userr
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
def signUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                return redirect('/')
            elif  User.objects.filter(email=email).exists():
                print('email taken')
                return redirect('/')
            else:    
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()  
                login(request,user)
                return redirect("/")
        else:
            print('password not matched')                
    return render(request,'signup.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def new(request): 
    if request.method == 'POST': 
        form=Postform(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('/') 
    else: 
        form = Postform()
    return render(request, 'new.html',{"form" : form}) 
   
