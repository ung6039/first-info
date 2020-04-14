from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def home_view(request):
    return render(request,"index.html", {})

def homework(request):
    return HttpResponse("<h1>인생은 B(brith) D(Death) 사이의 C(Chicken)이다.</h1>")


