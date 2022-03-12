from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from chats.models import *
from chats.forms import *

# Create your views here.

@login_required(login_url='lr')
def home(request):
    return render(request,'home.html')


@login_required(login_url='lr')
def services(request):
    return render(request,'services.html')


@login_required(login_url='lr')
def about(request):
    return render(request,'about.html')

@login_required(login_url='lr')
def contactview(request):
    return render(request,'contact.html')


@login_required(login_url='lr')
def search(request):
    return render(request,'search.html')


@login_required(login_url='lr')
def chatview(request):
    form=Chats_Form()
    res=chatmodel.objects.all()
    if request.method=='POST':
        form=Chats_Form(request.POST,request.FILES)
        if form.is_valid():
            chatmodel.objects.create(cid_id=request.user.id,
                                     message=form.cleaned_data['message'],
                                     files=form.cleaned_data['files'])
            return render(request,'chats.html',{'form':form,'res':res})
    return render(request,'chats.html',{'form':form,'res':res})


def cover(request):
    if not request.user.is_authenticated:
        return render(request,'cover.html')
    else:
        return redirect('home')
        

def loginview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Credentials')
                return redirect('login')
        return render(request,'login.html')
    else:
        return redirect('home')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'logout.html')
    else:
        return redirect('lr')

def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            p=request.POST['password']
            pa=request.POST['repassword']
            if p==pa:
                registermodel.objects.create(username=request.POST['username'],
                                        first_name=request.POST['firstname'],
                                        last_name=request.POST['lastname'],
                                        email=request.POST['email'],
                                        phone=request.POST['phone'],
                                        password=make_password(request.POST['password']),
                                        gender=request.POST['gender']),
            return redirect('login')

        return render(request,'register.html')
        
    else:
        return redirect('home')

def lr(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Error : Please login (OR) register')
        return render(request,'lr.html')
    else:
        return redirect('home')