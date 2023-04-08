from django.http import HttpRequest
from django.shortcuts import redirect, render,HttpResponse
from .models import Task
from .forms import Taskform


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = Taskform
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = Taskform(instance= task)
    if request.method == 'POST':
        form = Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,'update.html',context)


def deleteTask(request,pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request,'delete.html',context)
