from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Hospital.models import Report, Appointment, Doctor

def uploadreport(request, aid, did):
    if User.objects.filter(pk = request.user.id).exists():
        user= User.objects.get(pk = request.user.id)
    if Appointment.objects.filter(appointment_id = aid):
        appointment = Appointment.objects.get(appointment_id = aid)
    if Doctor.objects.filter(doctor_id = did):
        doctor = Doctor.objects.get(doctor_id = did)
        if request.method == 'POST':
            try:
                report_description = request.POST['report_description']
                report_pdf = request.FILES.get('report_pdf')
                
                if Report.objects.filter(appointment_id = aid).exists():
                    messages.error(request, "You have already uploaded your report for this appointment")
                    return redirect('listreport')
                else:
                    report = Report.objects.create (report_description = report_description, report_pdf = report_pdf, user= user, appointment = appointment, doctor = doctor)
                    report.save()
                    messages.success(request, 'You report has been uploaded successfully')
                    return redirect('listreport')
            except Exception as exp:
                res = ('Error!' + str(exp))
                messages.error(request, res)
                return redirect('admindashboard')
        else:
            return render(request, 'Reports/report.html')
    else:
        return render(request, 'Reports/report.html')


