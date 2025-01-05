from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def eduction(request):
    return render(request,'education.html')

def project(request):
    return render(request,'Projects.html')