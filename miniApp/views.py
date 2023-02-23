from django.shortcuts import render
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,"base.html")

def chkPermission(request):
    if 'userStatus' in request.session:
        userStatus = request.session['userStatus']
        if userStatus == 'customer':
            messages.add_message(request, messages.WARNING, "ท่านกำลังเข้าใช้ในส่วนที่ไม่ได้รับอนุญาต!!!")
            return False
        else:
            return True
    else:
        if Teacher.objects.count() != 0:
            messages.add_message(request, messages.WARNING, "ท่านกำลังเข้าใช้ในส่วนที่ไม่ได้รับอนุญาต!!!")
            return False
        else:
            return True

def userLogin(request):
    if request.method == "POST":
        userName = request.POST["userName"]
        userPass = request.POST["userPass"]
        user = authenticate(userName = userName, userPass = userPass)
        if user is not None:
            login(request, user)
            if user.is_staff == 0:
                teacher = Teacher.objects.get(teacherId = userName)
                request.session['userId'] = teacher.teacherId
                request.session['userFName'] = teacher.teacherFName
                request.session["userLName"] = teacher.teacherLName
                request.session['userStatus'] = "teacher"
            else:
                student = Student.objects.get(studentId=userName)
                request.session['userId'] = student.studentId
                request.session['userFName'] = student.studentFName
                request.session["userLName"] = student.studentLName
                request.session['userStatus'] = "student"
            messages.add_message(request, messages.INFO, "Login suscess...")
        else:
            messages.error(request, "USERNAME OR PASSWORD IS WRONG")
            data = {'userName': userName}
            return render(request,"userLogin.html", data)
    else:
        data = {'userName': ''}
        return render(request, 'userLogin.html', data)

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