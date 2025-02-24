from django.shortcuts import render
#from django.http import HttpResponse

def Bienvenido(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")




# Create your views here.
