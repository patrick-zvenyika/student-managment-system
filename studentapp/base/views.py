from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# # # Create your views here.
def LandingPage(request):
    return render(request,'index.html')

def RegisterPage(request):
    return render(request,'register1.html' )

def LoginPage(request):
    
    if request.method == 'POST':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not exist')
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Username OR Password does not exist')
    return render(request, 'login1.html')
