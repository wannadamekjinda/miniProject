from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")
def userLogin(request):
    return render(request,"userLogin.html")
def enroll_in1(request):
    return render(request,"enroll_in1.html")