from django.shortcuts import render
from django.shortcuts import redirect
from .models import Todo
from .forms import AddForm
from django.utils import timezone
import datetime
# Create your views here.

def todo_main(request):
    return render(request,"todo_main.html")

def todo_work(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    now = datetime.datetime.now()
    form = AddForm()
    todos = Todo.objects.all()
    data={
        "todos" : todos,
        "form": form,
        "now":now,
    }
    return render(request,"todo_work.html",data)

def todo_view(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    now = datetime.datetime.now()
    print(now)
    form = AddForm()
    todos = Todo.objects.all()
    data={
        "todos" : todos,
        "form": form,
        "now":now,
    }
    return render(request,"todo_list.html",data)

def toto_su(request,pk):
    print(pk)
    target =Todo.objects.get(pk=pk)
    target.is_done =True
    target.Todo_time = timezone.now()
    target.save()
    return redirect("todos")


def delete_todo(request,pk):
    target =Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todos")

def todo_back(request,pk):
    target = Todo.objects.get(pk=pk)
    print(target.is_done)
    target.is_done = False
    print(target.is_done)
    target.save()
    return redirect("todos")    


