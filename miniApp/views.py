from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")
def userLogin(request):
    return render(request,"userLogin.html")
def showRigister(request):
    return render(request,"showRigister.html")

def showSubject(request):
    return render(request,"showSubject.html")

