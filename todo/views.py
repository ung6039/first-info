from django.shortcuts import render
from .models import Todo
# Create your views here.

def todo_view(request):
    todos = Todo.objects.all()
    data={
        "todos" : todos,
    }
    return render(request, "todo_list.html",data)

def toto_su(request):
    todos =Todo.objects.all()
    data={
        "todos": todos,
    }
    return render(request,"todo_sucess.html",data)