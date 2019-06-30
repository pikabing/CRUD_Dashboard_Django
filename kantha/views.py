from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from . import forms
from . import models

def index(request):
    form = forms.AdminForm()
    return render(request, "index.html", {'form':form})
    
def login_admin(request):
    username = request.POST.get('username')
    password = request.POST.get("password")

    if(username == "pratik" and password == "password"):
        return redirect(reverse('dashboard'))
    else:
        form = forms.AdminForm()
        return render(request, "index.html",{'form':form})

def dashboard(request):
    return render(request, "header.html")


