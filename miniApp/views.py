from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")

def showSubject(request):
    return render(request,"showSubject.html")

def userLogin(request):
    return render(request,"userLogin.html")

def rigister(request):
    return render(request,'rigister.html')

def showRigister(request):
    return render(request,'showRigister.html')