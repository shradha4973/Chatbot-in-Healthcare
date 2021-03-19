from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, request
from Hospital.models import Doctor 

def home(request):
	doct  = Doctor.objects.all()
	return render(request,"Homepage/index.html", {'doct': doct})

def doctor(request):
	doctor  = Doctor.objects.all()	
	return render(request, "Appointments/appointment.html", context = {'doctor':doctor})

def single_doctor(request):
	return render(request, "DoctorPage/doctors-single.html")

