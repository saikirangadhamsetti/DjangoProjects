from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from admissions.forms import studentform,normalform,kk
from schoolapp.views import home as k
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required

@login_required
@permission_required("admissions_change")
def addadmission(request):
    kiran={"kiran1":studentform}
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        return redirect("/")
    return render(request,"admissions/addadmit.html",kiran)
@login_required
def kiran(request):
    m={"KK":normalform}
    if(request.method=='POST'):
        k=normalform(request.POST)
        l=k.__dict__
        return render(request,"index.html",l)
    return render(request,"admissions/addadmit.html",m)
def home(request):
    return HttpResponse("This is admissions home")
def send(request):
    p=models.student(name="kiran",phn="663092648")
    p.save()
    result= models.student.objects.values_list("id","name","phn").filter(name__contains="har")
    kiran={"kiran1":result}
    return render(request,"admissions/addadmission.html",kiran)
@login_required
def delete(request):
    form={"ki":kk}
    k=models.student.objects.values().all()
    m={"ll":k}
    if(request.method=="POST"):
        ki=kk(request.POST)
        print(ki.data["id"])
        s=models.student.objects.all().get(id=ki.data["id"])
        s.delete()
    return render(request,"admissions/addadmit.html",m)
def updatestudent(request,id):
    s=models.student.objects.get(id=id)
    form=studentform(instance=s)
    dict={"form":form}
    if request.method=='POST':
        form=studentform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,"admissions/update-admission.html",dict)
class classbasedview(View):
    def get(self,request):
        return HttpResponse("This is class based view")
class modellist(ListView):
    model=models.Teacher
class singledetail(DetailView):
    model=models.Teacher
class InsertTeacher(CreateView):
    model=models.Teacher
    fields=("name","subject","exp","contact")
class Updateteacher(UpdateView):
    model=models.Teacher
    fields=("name","exp","contact","subject")
class DeleteTeacher(DeleteView):
    model=models.Teacher
