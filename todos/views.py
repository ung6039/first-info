from django.shortcuts import render

from .models import Try_todo

# Create your views here.

def Todos_view(request):
    try_try = Try_todo.objects.all()
    data={
        "ename": try_try,
        "test": "11111",
        "advice":"성공은 실패의 어머니이다",
    }
    return render(request,"index-todo.html", data)