"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path
from post import views
#to import TemplateView,RedirectView
from django.views.generic.base import TemplateView,RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="homepage"),
    path("about/",views.about,name="aboutpage"),
    path("contact-us/",views.contact,name="contact"),
    path("Sweet/",views.product,name="sweet"),
    path("student/",views.student,name="student"),
    path("subject/",views.subject,name="subject"),
    path("take-data/",views.inputData,name="input"),
    path("submit/",views.submit,name="submit"),
    path("employee/",RedirectView.as_view(url="/admin"),name="employee"),
    path("view/",views.MyView.as_view(),name="classview"),
    path("template/",TemplateView.as_view(template_name="template.html",extra_context={"name":"Devaki"}),name="template"),
    path("students/",views.StudentView.as_view(),name="student")
]  #to create url use this and to see direct output keep it blank ""
