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
    path('admindashboard/', views.adminDashboard, name= 'admindashboard'),
    path('createdoctor/', views.adddoctor, name= 'createdoctor'),
    path('updatedoctor/<int:pk>', views.updatedoctor, name= 'updatedoctor'),
    path('deletedoctor/<int:pk>', views.deletedoctor, name= 'deletedoctor'),
    path('usertable/', views.usertable, name= 'usertable'),
    path('deleteuser/<int:uid>', views.deleteuser, name = 'deleteuser'),
    path('listappointment/', views.listappointment, name = 'listappointment'),
    path('updateappointment/<int:id>', views.updateappointment, name = 'updateappointment'),
    path('removeappointment/<int:aid>', views.removeappointment, name = 'removeappointment'),
    path('userfeedback/', views.userfeedback, name= 'userfeedback'),
    path('removefeedback/<int:fid>', views.removefeedback, name='removefeedback'),
    path('reportlist/', views.reportlist, name='reportlist'),
    path('downloadreports/<int:rid>', views.downloadreports, name='downloadreports'),
    path('removereport/<int:rid>', views.removereport, name='removereport'),
    path('usertransaction/', views.usertransaction, name = 'usertransaction'),
    path('removetransaction/<int:tid>', views.removetransaction, name = 'removetransaction'),
]
