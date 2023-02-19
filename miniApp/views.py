from django.shortcuts import render
from .models import *
# Create your views here.
def base(request):
    return render(request,"base.html")

def userLogin(request):
    return render(request,"userLogin.html")

def enroll_in1(request):
    return render(request,"enroll_in1.html")

def addRigister(request):
    return render(request,"addRigister.html")

def delRigister(request):
    return render(request,"delRigister.html")

def faculty(request):
    facultys = Faculty.objects.all().order_by('id')
    context = {'categories': facultys}
    return render(request,"CRUD/faculty.html", context)