
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path("", views.index,name="home"),
    path("/about", views.about,name="about"),
    path("/contact", views.contact,name="contact"),
    path("/register", views.register,name="register"),
    path("/login", views.login,name="login"),
    path("/submit", views.submit,name="submit"),
    path("/view", views.view,name="view"),
    path("submitted/", views.submitted,name="submitted"),
]