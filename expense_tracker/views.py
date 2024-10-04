from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

@login_required
def welcome(request):
    return render(request, 'welcome.html')

def logout_view(request):
    logout(request)
    return redirect('home')
