from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#create a function
def say_Hello(request):
    return render(request, "hello.html", {'name':"Katende Nicholas"})
