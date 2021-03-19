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
    path('profile/', views.profile, name='profile'),
    path('userappointment/', views.userappointment, name = 'userappointment'),
    path('updateprofile/', views.updateprofile, name = 'updateprofile'),
    path('userdelete/', views.userdelete, name='userdelete'),
    path('user_feedback', views.updatefeedback, name = 'user_feedback'),
    path('deletefeedback/', views.deletefeedback, name='deletefeedback'),
    path('deleteprofile/', views.deleteprofile, name='deleteprofile'),
    path('deletebackgroundImage', views.deletebackgroundImage, name='deletebackgroundImage'),
    path('listreport/', views.listreport, name = 'listreport'),
    path('deletereport/<int:rid>', views.deletereport, name='deletereport'),
    path('downloadreport/<int:rid>', views.downloadreport, name = 'downloadreport'),
    path('updatereport/<int:rid>', views.updatereport, name = 'updatereport'),
    path('updateamount/', views.updateamount, name = 'updateamount'),
    path('listtransaction/', views.listtransaction, name = 'listtransaction'),
    
    
   
]
