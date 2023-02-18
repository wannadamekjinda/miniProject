from django.db import models

# Create your models here.
from django.db.models import F, Sum, Count
import datetime

class Faculty(models.Model):
    facName = models.CharField(max_length=100, default="")
    facDesc = models.TextField(max_length=400)
    def __str__(self):
        return self.facName + ":" + self.facDesc

class MajorProgram(models.Model):
    majorProName = models.CharField(max_length=100, default="")
    majorProDesc = models.TextField(max_length=400)

    def __str__(self):
        return self.majorProName + ":" + self.majorProDesc

class Major(models.Model):
    majorName = models.CharField(max_length=100, default="")
    majorDesc = models.TextField(max_length=400)

    def __str__(self):
        return self.majorName + ":" + self.majorDesc

class Subject(models.Model):
    subjectId   = models.CharField(max_length=15, primary_key=True, default="")
    subjectName = models.CharField(max_length=50, default="")
    subjectCredit = models.IntegerField(max_length=1, default="1")

    def __str__(self):
        return self.subjectId + ":" + self.subjectName + ":" + str(self.subjectCredit)

class Gender(models.Model):
    genName = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.genName

class Student(models.Model):
    studentId = models.CharField(max_length=15, primary_key=True, default="")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)
    studentFName = models.CharField(max_length=50, default="")
    studentLName = models.CharField(max_length=50, default="")
    studentAddress = models.TextField(max_length=400, default="")
    studentBirthdate = models.DateField(default=None)

    def __str__(self):
        return self.studentId + ":" + self.gender.genName + ":" + self.studentFName + ":" + self.studentLName

class Teacher(models.Model):
    teacherId = models.CharField(max_length=15, primary_key=True, default="")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)
    teacherFName = models.CharField(max_length=50, default="")
    teacherLName = models.CharField(max_length=50, default="")
    teacherAddress = models.TextField(max_length=400, default="")
    teacherBirthdate = models.DateField(default=None)

    def __str__(self):
        return self.teacherId + ":" + self.gender.genName + ":" + self.teacherFName + ":" + self.teacherLName

class register(models.Model):
    resgisId = models.CharField(max_length = 15, primary_key=True, default="")
    resgisDate = models.DateTimeField(auto_now_add = True)
