from django.shortcuts import render, redirect
from Hospital.models import Doctor, Appointment, Transaction, Profile
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login_user')
def appointment(request):
    doctor = Doctor.objects.all()
    return render (request, "Appointments/appointment.html", context = {'doctor': doctor})

@login_required(login_url='login_user')
def createappointment(request, did):
    if Doctor.objects.filter(doctor_id = did):
        doctor = Doctor.objects.get(doctor_id = did)
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
    if Profile.objects.filter(pk = request.user.id):
        profile = Profile.objects.get(pk = request.user.id)
    if request.method == "POST":
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        price = request.POST['price']
        message = request.POST['message']

        if doctor.appointment_price > user.profile.user_amount:
            messages.error(request, "You do not have sufficient balance")
            return redirect('createappointment', did = doctor.doctor_id)
        elif user.profile.user_amount >= doctor.appointment_price:
            payment=(int(user.profile.user_amount))-(int(doctor.appointment_price))
            user.profile.user_amount = payment
            user.profile.save()
            appointment = Appointment.objects.create(appointment_date = appointment_date, appointment_time = appointment_time, message = message, user = user, doctor = doctor)
            transaction = Transaction.objects.create(price = price, user = user, doctor = doctor, appointment = appointment)
            appointment.save()
            transaction.save()
            messages.success(request, "You have booked an appointment")
            return redirect('createappointment', did = doctor.doctor_id)
    else:
        return render (request, "Appointments/createappointment.html", context = {'doctor': doctor})




 





    