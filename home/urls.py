from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('trainee',views.trainee_view,name="trainee"),
    path('faculty',views.faculty_view,name="faculty"),
    path('courses',views.courses_view,name="courses"),
    path('add_trainee',views.add_trainee,name="add_trainee"),
    path('add_faculty',views.add_faculty,name="add_faculty"),
    path('add_courses',views.add_courses,name="add_courses"),
    path('edit_trainee',views.edit_trainee,name="edit_trainee"),
    path('edit_faculty',views.edit_faculty,name="edit_faculty"),
    path('edit_courses',views.edit_courses,name="edit_courses"),
    path('update_trainee/<str:id>',views.update_trainee,name="update_trainee"),
    path('update_faculty/<str:id>',views.update_faculty,name="update_faculty"),
    path('update_courses/<str:id>',views.update_courses,name="update_courses"),
    path('delete_trainee/<str:id>',views.delete_trainee,name="delete_trainee"),
    path('delete_faculty/<str:id>',views.delete_faculty,name="delete_faculty"),
    path('delete_courses/<str:id>',views.delete_courses,name="delete_courses"),
    path('trainee_search',csrf_exempt(views.trainee_search),name="trainee_search"),
    path('faculty_search',csrf_exempt(views.faculty_search),name="faculty_search"),
    path('courses_search',csrf_exempt(views.courses_search),name="courses_search"),
    path('infra',views.infra_view,name="infra"),
    path('export_excel_trainee',views.export_excel_trainee,name="export_excel_trainee"),
    path('export_excel_faculty',views.export_excel_faculty,name="export_excel_faculty"),
    path('export_excel_courses', views.export_excel_courses, name="export_excel_courses")

]