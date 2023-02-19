from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Faculty)
admin.site.register(MajorProgram)
admin.site.register(Major)
admin.site.register(Gender)