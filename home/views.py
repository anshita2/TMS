from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Trainee_model
import json
from django.http import JsonResponse
from django.core.paginator import Paginator

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
    paginator=Paginator(trainee_obj,5)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator,page_number)
    context={
        'trainee_obj':trainee_obj,   #dictionary
        'page_obj':page_obj,
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

def trainee_search(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get('searchtext','')
        search_trainee=Trainee_model.objects.filter(name__startswith=search_str) | Trainee_model.objects.filter(course__startswith=search_str) | Trainee_model.objects.filter(domain__startswith=search_str)
        data=search_trainee.values()
        return JsonResponse(list(data),safe=False)