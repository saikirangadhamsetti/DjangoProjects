from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
    todo=Todo.objects.all()
    m={"todos":todo}
    if request.method=='POST':
        if(request.POST["title"]!=""):
            new_todo=Todo(title=request.POST["title"])
            new_todo.save()
        else:
            K={"msg":"Please enter a task"}
            return render(request,"index.html",K)
        return redirect('/')
    return render(request,"index.html",m)
def delete(request,id):
    k=Todo.objects.get(id=id)
    k.delete()
    return redirect("/")