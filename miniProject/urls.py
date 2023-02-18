"""miniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miniApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base, name='base'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('delRigister', views.addRigister, name='addRigister'),
    path('addRigister', views.delRigister, name='delRigister'),
    path('enroll_in1',views.enroll_in1,name='enroll_in1'),

    #CRUD
    path('faculty', views.faculty,name="faculty")
]
