
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('about', views.about,name='about'),
    path('service', views.service,name='service'),
    path('contact', views.contact,name='contact'),
    path('Detail/<ilabel>',views.Detailpage),
    path("search", views.search, name='search'),


    path("signpin", views.signpin, name='signpin'),
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),


    path("logout", views.logout, name='logout')


    ]