from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Trainee_model
import json
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator
from .models import Course_model
from .models import Faculty_model
import datetime
import xlwt


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

def logout_view(request):
    logout(request)
    return redirect('/login')
    
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

def faculty_view(request):
    faculty_obj=Faculty_model.objects.all()
    paginator=Paginator(faculty_obj,5)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator,page_number)
    context={
        'faculty_obj':faculty_obj,   #dictionary
        'page_obj':page_obj,
    }
    return render(request,'manage_faculty.html',context)

def courses_view(request):
    courses_obj=Course_model.objects.all()
    paginator=Paginator(courses_obj,5)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator,page_number)
    context={
        'courses_obj':courses_obj,   #dictionary
        'page_obj':page_obj,
    }
    return render(request,'manage_courses.html',context)

def infra_view(request):
    return render(request,'infra.html')

def add_trainee(request):
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


def add_faculty(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        category=request.POST.get("category")
        faculty_data=Faculty_model(name=name , phone=phone , email=email , category=category)
        faculty_data.save()
        return redirect('/faculty')
    return render(request,'manage_faculty.html')


def add_courses(request):
    if request.method=="POST":
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        venue_name = request.POST.get("venue_name")
        trainees_enrolled = request.POST.get("trainees_enrolled")
        faculty = request.POST.get("faculty")
        course_data = Course_model(
            name=name,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            venue_name=venue_name,
            trainees_enrolled=trainees_enrolled,
            faculty=faculty,
        )
        course_data.save()
        return redirect('/courses')
    return render(request,'manage_courses.html')

def edit_trainee(request):
    trainee_obj=Trainee_model.objects.all()
    context={
        'trainee_obj':trainee_obj,   #dictionary
    }
    return render(request,'trainee.html',context)

def edit_faculty(request):
    faculty_obj=Faculty_model.objects.all()
    context={
        'faculty_obj':faculty_obj,   #dictionary
    }
    return render(request,'manage_faculty.html',context)

def edit_courses(request):
    courses_obj=Course_model.objects.all()
    context={
        'courses_obj':courses_obj,   #dictionary
    }
    return render(request,'manage_courses.html',context)

def update_trainee(request,id):
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

def update_faculty(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        category=request.POST.get("category")
        faculty_data=Faculty_model(id=id,name=name , phone=phone , email=email , category=category)
        faculty_data.save()
        return redirect('/faculty')
    return redirect('/faculty')

def update_courses(request,id):
    if request.method=='POST':
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        venue_name = request.POST.get("venue_name")
        trainees_enrolled = request.POST.get("trainees_enrolled")
        faculty = request.POST.get("faculty")
        course_data = Course_model(
            id=id,
            name=name,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            venue_name=venue_name,
            trainees_enrolled=trainees_enrolled,
            faculty=faculty,
        )
        course_data.save()
        return redirect('/courses')
    return redirect('/courses')

def delete_trainee(request,id):
    emp=Trainee_model.objects.filter(id=id)
    emp.delete()
    return redirect('/trainee')

def delete_faculty(request,id):
    emp=Faculty_model.objects.filter(id=id)
    emp.delete()
    return redirect('/faculty')

def delete_courses(request,id):
    emp=Course_model.objects.filter(id=id)
    emp.delete()
    return redirect('/courses')

def trainee_search(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get('searchtext','')
        search_trainee=Trainee_model.objects.filter(name__startswith=search_str) | Trainee_model.objects.filter(course__startswith=search_str) | Trainee_model.objects.filter(domain__startswith=search_str)
        data=search_trainee.values()
        return JsonResponse(list(data),safe=False)


def faculty_search(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get('searchtext','')
        search_faculty=Faculty_model.objects.filter(name__startswith=search_str)
        data=search_faculty.values()
        return JsonResponse(list(data),safe=False)
    

def courses_search(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get('searchtext','')
        search_courses=Course_model.objects.filter(name__startswith=search_str)
        data=search_courses.values()
        return JsonResponse(list(data),safe=False)
    
def export_excel_trainee(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Trainee '+ \
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Trainee')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['Name','Phone','Email','Course enrolled' , 'Domain']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style=xlwt.XFStyle()
    rows=Trainee_model.objects.values_list('name' , 'phone' , 'email' , 'course' , 'domain')

    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)
    return response

def export_excel_faculty(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Faculty '+ \
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Faculty')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['Name','Email','Phone' ,'Category']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style=xlwt.XFStyle()
    rows=Faculty_model.objects.values_list('name' , 'email' , 'phone' , 'category' )

    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)
    return response

def export_excel_courses(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Courses '+ \
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Courses')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['Course Name','Duration','Start date','End date' , 'Venue name' ,'Trainees enrolled' ,'Faculty']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style=xlwt.XFStyle()
    rows=Course_model.objects.values_list('name' , 'duration' , 'start_date' , 'end_date' , 'venue_name' , 'trainees_enrolled','faculty')

    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)
    return response