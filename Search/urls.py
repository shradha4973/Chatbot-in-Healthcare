"""HospitalManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search_doctor/', views.search_doctor, name='search_doctor'),
    path('search_user/', views.search_user, name='search_user'),
    path('search_appointments/', views.search_appointments, name='search_appointments'),
    path('search_feedbacks/', views.search_feedbacks, name='search_feedbacks'),
    path('search_transactions/', views.search_transactions, name='search_transactions'),
    path('search_reports/', views.search_reports, name='search_reports'),
    path('search_listtransactions/', views.search_listtransactions, name='search_listtransactions'),
    path('search_report/', views.search_report, name='search_report'),
    path('search_appointment/', views.search_appointment, name='search_appointment'),

     
   
]
