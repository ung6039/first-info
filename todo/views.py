from django.shortcuts import render
from django.shortcuts import redirect
from .models import Todo
from .forms import AddForm
# Create your views here.

def todo_view(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddForm()
    todos = Todo.objects.all()
    data={
        "todos" : todos,
        "form": form,
    }
    return render(request,"todo_list.html",data)

def toto_su(request):
    todos =Todo.objects.all()
    data={
        "todos": todos,
        
    }
    return render(request,"todo_sucess.html",data)

def delete_todo(request,pk):
    target =Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todos")
    