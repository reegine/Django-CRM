from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    #check to see i the user is already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenthicate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In")
            return redirect('home')
        else : 
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('home')
    else: 
        return render(request, 'home.html', {}) 

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {}) 
