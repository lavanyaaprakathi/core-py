from django.shortcuts import render,redirect

# Create your views here.

from home.forms import EmployeeForm
from home.models import Employee


def home(request):
   
    if request.method == "POST": 
        form = EmployeeForm(request.POST) 
        if form.is_valid(): 
           try: 
             form.save() 
             return redirect('/') 
           except: 
                 pass
    else: 
      form = EmployeeForm()
      
    return render(request, "index.html",{'form':form})




def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")
