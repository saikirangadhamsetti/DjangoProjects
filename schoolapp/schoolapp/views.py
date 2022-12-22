from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request,"index.html")
def login(request):
    return render(request,"reg")
def logout(request):
    return render(request,"logout.html")