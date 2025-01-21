from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('trainee',views.trainee_view,name="trainee"),
    path('add',views.add,name="add"),
    path('edit',views.edit,name="edit"),
    path('update/<str:id>',views.update,name="update"),
    path('delete/<str:id>',views.delete,name="delete")
]