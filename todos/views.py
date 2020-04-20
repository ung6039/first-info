from django.shortcuts import render

from .models import Todos

# Create your views here.

def Todos_view(request):
    Todos =Todos.objects.all()
    data={
        "todos": Todos,
    }
    return render(request,"index-todo.html",data)