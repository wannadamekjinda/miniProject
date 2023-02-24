from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Faculty)
admin.site.register(MajorProgram)
admin.site.register(Major)
admin.site.register(Gender)
admin.site.register(StudentStatus)
admin.site.register(EducationLevel)
admin.site.register(LearnGroup)
admin.site.register(StudentSubject)
admin.site.register(SubjectList)
