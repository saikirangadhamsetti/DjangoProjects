from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def feecollection(request):
    return HttpResponse('I will update the fee collected from you in this view')
def feeDuesReport(request):
    return HttpResponse('I will track ur previous data and display your feeDueReport in this view')
def feeCollectionReport(request):
    return HttpResponse("I will display the feeCollected till now from you")
def home(request):
    return HttpResponse("I am finance home")
