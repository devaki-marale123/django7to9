
from email import message
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate

# home ......................
def home(request):
    return render(request,"index.html")

#Register page
# -------------------
def register(request):
    message=None
    if request.method=="GET":
        #form=UserCreationForm()
        form=CustomUserCreationForm()
    if request.method=="POST":  
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            message="User registration Successful"
        else:
            message="User registration Failed" 
    
    return render(request,'register.html',{'form':form,'message':message})    
#userlogin
#===============================================================================

def user_login(request):
    if request.method=="GET":
        return render(request,"login.html")
    if request.method=="POST":
        #fetching data from input fields 
        username=request.POST.get("username")
        password=request.POST.get("password")


        # using authenticate function to check credentials
        user=authenticate(username=username,password=password)
        if user is None:
             message="Login Failed"
             return render(request,"login.html",{"message":message})


        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/products/")

#user logout
# ============================================================
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


# demo function for template-filter

def template_filter_example(request):
    data="Hello I am learning Template Filter"    
    return render(request,"demo.html",{"data":data})


