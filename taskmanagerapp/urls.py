from django.contrib import admin
from django.urls import path 
from taskmanagerapp import views

urlpatterns = [
    path("" , views.index , name = "home"),
    path("about" , views.about , name = "about"),
    path("contact" , views.contact , name = "contact"),
    path("signup" , views.signup , name = "signup"),
    path("login" , views.LoginPage , name = "login"),
    path("dashboard" , views.dashboard , name = "dashboard"),
    path("logout" , views.LogoutPage , name = "logout"),
    path("add_todo" , views.add_todo , name = "add_todo"),
    path("delete_todo<int:id>" , views.delete_todo , name = "delete_todo"),
    path("change_status<int:id>/<str:status>" , views.change_todo , name = "change_todo")

    
]
