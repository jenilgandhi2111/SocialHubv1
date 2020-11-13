from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login(request):
    return render(request,'login/base.html')

def login_user(request):
    # Only for post requests as this is routing page.
    if request.method=='GET':
        return HttpResponse("<h1>ERROR 404 PAGE NOT FOUND</h1>")
    else:
        email=request.POST.get('login')
        password=request.POST.get('password')
        user = authenticate(request,username=email, password=password)
        if user is not None:
            auth_login(request,user)
            print("jenil logged in")
            return redirect('http://localhost:8000/home')
        else:
            print("check login or password details")
    return HttpResponse("4040")
    
