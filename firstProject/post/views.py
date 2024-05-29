import http
from pipes import Template
from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return HttpResponse("This is first view...")

def about(request):
    return HttpResponse("My Name Is DEVAKI")

def contact(request):
   
    return render(request,"contact.html",{"name":"Nikita","address":"Mumbai","school":"Vikas School"})

def product(request):
    return render(request,"product.html",{"Sweet1":"Kajukatali","Sweet2":"Gulab Jamun","Sweet3":"Jalebi"})

def employee(request):
    employees={"101":{"name":"Manoj","age":25,"salary":50000},
    "102":{"name":"Nisha","age":29,"salary":35000}}
    return render(request,"employee.html",{"employees":employees})

def student(request):
    student={"0001":{"name":"Nikita Raut","Class":"5th","Percentage":"78%"},
    "0002":{"name":"Shrutika Jadhav","Class":"6th","Percentage":"89%"},
    "0003":{"name":"Shrutika Jadhav","Class":"6th","Percentage":"89%"},
    "0004":{"name":"Shrutika Jadhav","Class":"6th","Percentage":"89%"}
    }
    return render(request,"student.html",{"student":student})
    
def subject(request):
     return render(request,"subject.html",{"subject":["Maths","English","Hindi","Marathi","History"]})
def inputData(request):
    return render(request,"data.html") 
def submit(request):
    if request.method=="GET":
        return HttpResponse("You are not allowded to be here through GET")
    elif request.method=="POST":    
    # username=request.GET.get("username")
        username=request.POST.get("username")
        phoneno=request.POST.get("phoneno")
        print(username)

        return render(request,"data.html",{"username":username,"phoneno":phoneno})  
#functions 
# .....
# ......
class MyView(View):
    def get(self,request):
       # return HttpResponse("<h1>First Class Based View</h1>")
        return render(request,"myview.html")
    def post(self,request):
        username=request.POST.get("username")
        city=request.POST.get("city")
        return render(request,"myview.html",{"username":username,"city":city}) 

#####..............
#Template View
class StudentView(TemplateView):
    template_name="studentview.html"
    def get_context_data(self):
        context=super().get_context_data()
        context["name"]="Janaki"
        context["age"]=18
        return context





    





