from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Trainee_model

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request,'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    return render(request, 'login.html')
    
def trainee_view(request):
    trainee_obj=Trainee_model.objects.all()
    context={
        'trainee_obj':trainee_obj,   #dictionary
    }
    return render(request,'trainee.html',context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def add(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        course=request.POST.get("course")
        domain=request.POST.get("domain")
        trainee_data=Trainee_model(name=name , phone=phone , email=email , course=course , domain=domain)
        trainee_data.save()
        return redirect('/trainee')
    return render(request,'trainee.html')

def edit(request):
    trainee_obj=Trainee_model.objects.all()
    context={
        'trainee_obj':trainee_obj,   #dictionary
    }
    return render(request,'trainee.html',context)

def update(request,id):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        course=request.POST.get("course")
        domain=request.POST.get("domain")
        trainee_data=Trainee_model(id=id,name=name , phone=phone , email=email , course=course , domain=domain)
        trainee_data.save()
        return redirect('/trainee')
    return redirect('/trainee')

def delete(request,id):
    emp=Trainee_model.objects.filter(id=id)
    emp.delete()
    return redirect('/trainee')