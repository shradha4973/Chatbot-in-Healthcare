from django.shortcuts import render, redirect
from django.http import HttpResponse
from Hospital.models import Doctor, Profile, Appointment, Feedback, Report, Transaction
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
   
def adddoctor(request):
    firstName = ''
    lastName = ''
    emailAddress = ''
    specialization = ''
    qualification = ''
    appointment_price = ''
    profileImage = ''
    backgroundImage = ''
    if request.method == 'POST':
        try:
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            emailAddress = request.POST['emailAddress']
            specialization = request.POST['specialization']
            qualification = request.POST['qualification']
            appointment_price = request.POST['appointment_price']
            profileImage = request.FILES.get('profileImage')
            backgroundImage = request.FILES.get('backgroundImage')
            
            if (firstName == '' or lastName == '' or emailAddress == '' or qualification == '' or specialization == ''):
                raise Exception ('Empty Field')
            elif profileImage.content_type != 'image/jpeg' and profileImage.content_type != 'image/png':
                raise Exception ('Image type error')
            elif (int(appointment_price) < 0):
                raise Exception('Price cannot be negative')
            elif Doctor.objects.filter(emailAddress = emailAddress).exists():
                messages.error(request, 'email address already in use')
                return redirect('createdoctor')
            else:
                doctor = Doctor.objects.create(firstName = firstName, lastName = lastName, emailAddress = emailAddress, specialization = specialization,  qualification = qualification, appointment_price = appointment_price, profileImage = profileImage, backgroundImage = backgroundImage)
                doctor.save()
                messages.success(request, "Doctor added successfully. ")
                return redirect('createdoctor')
        except Exception as exp:
            res = (str (exp))
            messages.error(request, res)
            return redirect('createdoctor')
    else:
        return render(request, 'AdminDashboard/createdoctor.html', context={
            'firstName': firstName,
            'lastName' : lastName,
            'emailAddress': emailAddress,
            'qualification': qualification,
            'specialization' : specialization,
            'appointment_price': appointment_price,
            'profileImage': profileImage,
            'backgroundImage': backgroundImage
        })
        
def adminDashboard(request):
    doctors = Doctor.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(doctors, 10)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/admindashboard.html', context = {'doctors': doctors})

def updatedoctor(request, pk):
    if Doctor.objects.filter(doctor_id = pk):
        doctors = Doctor.objects.get(doctor_id = pk)
        if request.method == 'POST':
            try:
                firstName = request.POST['firstName']
                lastName = request.POST['lastName']
                emailAddress = request.POST['emailAddress']
                qualification = request.POST['qualification']
                specialization = request.POST['specialization']
                appointment_price = request.POST['appointment_price']
                profileImage = request.FILES.get('profileImage', None)
                backgroundImage = request.FILES.get('backgroundImage', None) 
                if (profileImage == None and backgroundImage == None and int(appointment_price) < 0):
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                elif profileImage == None and int(appointment_price)<0:
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.backgroundImage = backgroundImage
                elif profileImage == None:
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.appointment_price = appointment_price
                    doctors.backgroundImage = backgroundImage
                elif backgroundImage == None:
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.appointment_price = appointment_price
                    doctors.profileImage = profileImage  
                elif backgroundImage == None and int(appointment_price) < 0:
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.profileImage = profileImage
                elif (profileImage == None and backgroundImage == None):
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.appointment_price = appointment_price
                elif (int(appointment_price) < 0):
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.profileImage = profileImage  
                    doctors.backgroundImage = backgroundImage

                else: 
                    doctors.firstName=firstName
                    doctors.lastName=lastName
                    doctors.emailAddress = emailAddress
                    doctors.qualification = qualification
                    doctors.specialization = specialization
                    doctors.profileImage = profileImage
                    doctors.appointment_price = appointment_price
                    doctors.backgroundImage = backgroundImage 
                    
                doctors.save()
                messages.success(request, "Doctor updated successfully. ")
                return redirect('../admindashboard', pk = doctors.doctor_id)

            except Exception as ex:
                res = ('ERROR!' + str(ex))
                messages.error(request,res)
                return redirect('updatedoctor', pk = doctors.doctor_id)
        else:
                return render (request, 'AdminDashboard/userprofile.html', {'doctors': doctors})
    else:
        messages.error(request, "Couldn't find the doctor")
        return redirect('../admindashboard')

def deletedoctor(request, pk):
    try:
        if Doctor.objects.filter(doctor_id = pk).exists():
            doctors = Doctor.objects.get(doctor_id= pk)
            doctors.delete()
            messages.success(request, "Doctor removed successfully")
            return redirect ('../admindashboard')
        else:
            messages.error(request, "Error occurred while deleting doctor")
            return redirect(request, '../admindashboard')
    except Exception as exp:
        res = ('ERROR'+ str(ex))
        messages.error(request,res)
        return redirect('/', pk = doctors.doctor_id)


def usertable(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/usertable.html', {'user_list': user_list})

def deleteuser(request, uid):
    if User.objects.filter(id = uid).exists():
        user_list = User.objects.get(id= uid)
        user_list.delete()
        messages.success(request, "User deleted successfully")
        return redirect ('../usertable')
    else:
        messages.error(request, "Error occurred while deleting user")
        return redirect(request, '../usertable')

def listappointment(request):
    appointments = Appointment.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(appointments, 10)
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/listappointments.html', {'appointments': appointments})

def updateappointment(request, id=None):
    if Appointment.objects.filter(appointment_id = id):
        appointment = Appointment.objects.get(appointment_id = id)
        if request.method == 'POST':
            try:
                appointment_date = request.POST['appointment_date']
                appointment_time = request.POST['appointment_time']

                if appointment_date == None:
                    appointment.appointment_time = appointment_time

                elif appointment_time == None:
                    appointment.appointment_date = appointment_date

                else:
                    appointment.appointment_date = appointment_date
                    appointment.appointment_time = appointment_time
                appointment.save()
                messages.success(request, "Appointment updated successfully")
                return redirect('listappointment')
            except Exception as exp:
                res = ('ERROR'+ str(exp))
                messages.error(request, res)
                return redirect('listappointment')     
        else:
            messages.error(request, "Error! Failed to update appointment")
            return render(request, "AdminDashboard/updateappointment.html",context = {'appointment':appointment})
    else:
        messages.error(request, "Error")
        return redirect('listappointment')

def removeappointment(request, aid):
    if Appointment.objects.filter(appointment_id = aid).exists():
        removeappointment = Appointment.objects.get(appointment_id = aid)
        removeappointment.delete()
        messages.success(request, "Appointment removed successfully")
        return redirect('listappointment')

def userfeedback(request):
    feedback = None
    feedback = Feedback.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(feedback, 10)
    try:
        feedback = paginator.page(page)
    except PageNotAnInteger:
        feedback = paginator.page(1)
    except EmptyPage:
        feedback = paginator.page(paginator.num_pages)
    return render(request, "AdminDashboard/userfeedback.html", context = {'feedback': feedback})

def removefeedback(request, fid):
    if Feedback.objects.filter(id = fid).exists():
        removefeedback = Feedback.objects.get(id = fid)
        removefeedback.delete()
        messages.success(request, "Feedback removed successfully")
        return redirect('userfeedback')

def reportlist(request):
    reports = Report.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(reports, 10)
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/usersreport.html', context={'reports': reports})

def downloadreports(request, rid):
    if Report.objects.filter(id= rid).exists():
        report = Report.objects.get(pk = rid)
        file = report.report_pdf
        response = HttpResponse(file, content_type='application/pdf')
        response['Content-Disposition'] =  report.report_pdf
        return response
    else:
      messages.error(request,"Problem while converting file to Pdf")
      return redirect("listreport")

def removereport(request, rid):
    if Report.objects.filter(id = rid).exists():
        removereport = Report.objects.get(id = rid)
        removereport.delete()
        messages.success(request, 'Report deleted successfully')
        return redirect('reportlist')

def usertransaction(request):
    transaction = Transaction.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(transaction, 10)
    try:
        transaction = paginator.page(page)
    except PageNotAnInteger:
        transaction = paginator.page(1)
    except EmptyPage:
        transaction = paginator.page(paginator.num_pages)
    return render (request, 'AdminDashboard/usertransaction.html', context = {'transaction': transaction})

def removetransaction(request, tid):
    if Transaction.objects.filter(id = tid).exists():
        transaction = Transaction.objects.get(id = tid)
        transaction.delete()
        messages.success(request, 'Transaction removed successfully')
        return redirect('usertransaction')



   

   
    
   

    

