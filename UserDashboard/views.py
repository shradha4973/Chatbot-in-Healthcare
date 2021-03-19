from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from Hospital.models import Profile, Appointment, Doctor, Feedback, Report, Transaction
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    
def profile(request):
    return render (request, 'UserDashboard/profile.html')

def updateprofile(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
        profile = Profile.objects.filter(pk = request.user.id)
        if request.method == 'POST':
            try:
                username = request.POST['username']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                age = request.POST['age']
                user_bio = request.POST['user_bio']
                userprofileImage = request.FILES.get('userprofileImage', None)
                userbackgroundImage = request.FILES.get('userbackgroundImage', None)
                
                if (userprofileImage == None and userbackgroundImage == None):
                    user.username = username
                    user.first_name=first_name
                    user.last_name=last_name
                    user.email = email
                    user.profile.age = age
                    user.profile.user_bio = user_bio
                elif(userprofileImage == None):
                    user.username = username
                    user.first_name=first_name
                    user.last_name=last_name
                    user.email = email
                    user.profile.age = age
                    user.profile.user_bio = user_bio
                    user.profile.userbackgroundImage = userbackgroundImage
                elif(userbackgroundImage == None):
                    user.username = username
                    user.first_name=first_name
                    user.last_name=last_name
                    user.email = email
                    user.profile.age = age
                    user.profile.user_bio = user_bio
                    user.profile.userprofileImage = userprofileImage
                else:
                    user.username = username
                    user.first_name=first_name
                    user.last_name=last_name
                    user.email = email
                    user.profile.age = age
                    user.profile.user_bio = user_bio
                    user.profile.userprofileImage = userprofileImage
                    user.profile.userbackgroundImage = userbackgroundImage 
                user.save()
                user.profile.save()
                messages.success(request, "Your profile is updated successfully")
                return redirect('updateprofile')
            except Exception as ex:
                res = ('ERROR'+ str(ex))
                messages.error(request, res)
                return redirect('updateprofile')
        else:
            return render (request, 'UserDashboard/updateuserprofile.html')
    else:
        messages.error(request, "Sorry! Error occurred during data processing")
        return redirect('updateprofile')

def deleteprofile(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
        profile.userprofileImage = Profile.objects.get(user_id = user.id)
        user.profile.userprofileImage.delete()
        messages.success(request, "Profile removed successfully")
        return redirect('updateprofile')
    else:
        messages.error(request, 'Error while processing data')
        return redirect('updateprofile')

def deletebackgroundImage(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
        profile.userbackgroundImage = Profile.objects.get(user_id = user.id)
        user.profile.userbackgroundImage.delete()
        messages.success(request, "Cover image removed successfully")
        return redirect('updateprofile')
    else:
        messages.error(request, 'Error while processing data')
        return redirect('updateprofile')

def userdelete(request):
    if User.objects.filter(pk = request.user.id).exists():
        user = User.objects.get(pk = request.user.id)
        user.delete()
        return redirect ('/')
    else:
        return redirect('/')

def userappointment(request):
    u = User.objects.get(pk = request.user.id)
    appointment = Appointment.objects.filter(user_id = u.id)
    page = request.GET.get('page', 1)
    paginator = Paginator(appointment, 10)
    try:
        appointment = paginator.page(page)
    except PageNotAnInteger:
        appointment = paginator.page(1)
    except EmptyPage:
        appointment = paginator.page(paginator.num_pages)
    return render(request, 'UserDashboard/userappointment.html', {'appointment': appointment})

def updatefeedback(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk= request.user.id)
        feedback = Feedback.objects.filter(user_id = user.id)
        if request.method == 'POST':
            try:
                feedback = request.POST['feedback']
                user.feedback.feedback = feedback
                user.feedback.save()
                messages.success(request, 'Your feedback has updated successfully')
                return redirect('user_feedback')
            except Exception as exp:
                res =  (str (exp))
                messages.error(request, res)  
        else:
             return render(request, 'UserDashboard/feedback.html', context = {'feedback': feedback})
    else:
        messages.error(request, 'Error while processing data')
        return render(request,'UserDashboard/feedback.html')

def deletefeedback(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
        feedback = Feedback.objects.get(user_id = user.id)
        user.feedback.delete()
        messages.success(request, "Feedback removed successfully")
        return redirect('userfeedback')
    else:
        messages.error(request, 'Error while processing data')
        return redirect('userfeedback')

def listreport(request):
    user = User.objects.get(pk = request.user.id)
    report = Report.objects.filter(user_id = user.id)
    page = request.GET.get('page', 1)
    paginator = Paginator(report, 1)
    try:
        report = paginator.page(page)
    except PageNotAnInteger:
        report = paginator.page(1)
    except EmptyPage:
        report = paginator.page(paginator.num_pages)
    return render (request, 'UserDashboard/reports.html', context = {'report': report})


def deletereport(request, rid):
    if Report.objects.filter(id= rid).exists():
        report = Report.objects.get(pk = rid)
        report.delete()
        messages.success(request, 'You have sucessfully delete report')
        return redirect('listreport')
    else:
        messages.error(request, 'Error while deleting report')
        return redirect('listreport')

def downloadreport(request, rid):
    if Report.objects.filter(id= rid).exists():
        report = Report.objects.get(pk = rid)
        file = report.report_pdf
        response = HttpResponse(file, content_type='application/pdf')
        response['Content-Disposition'] =  report.report_pdf
        return response
    else:
      messages.error(request,"Problem while converting file to Pdf")
      return redirect("listreport")

def updatereport(request, rid):
    if Report.objects.filter(id = rid).exists():
        report = Report.objects.get(pk = rid)
        if request.method == 'POST':
            try:
                report_pdf = request.FILES.get('report_pdf')
                report_description = request.POST['report_description']  
                if report_description == None:
                    report.report_pdf = report_pdf
                elif report_pdf == None:
                    report.report_description = report_description
                elif (report_pdf == None and report_description == None):
                    return redirect('listreport')
                else:
                    report.report_pdf = report_pdf
                    report.report_description = report_description
                report.save()
                messages.success(request, 'You have successfully update the report')
                return redirect('listreport')
            except Exception as exp:
                res= (str (exp))
                messages.error(request, res)  
                return redirect('listreport')
        else:
            return render(request, 'Reports/report.html')
    else:
        return render(request, 'Reports/report.html')

def updateamount(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.filter(user_id =user.id).get()
        user_amount = request.POST.get('user_amount',0)
        
        if (int(user_amount) <= 0):
            messages.error(request, "Your amount must be positive number")
            return redirect('updateamount')
        else:
            profile.user_amount = int(profile.user_amount) + int(user_amount)
            profile.save()
            messages.success(request, 'Amount updated successfully')
            return redirect('updateamount')
    else:
        return render(request, 'UserDashboard/updateamount.html')

def listtransaction(request):
    if User.objects.filter(pk = request.user.id).exists():
        user = User.objects.get(pk = request.user.id)
        listtransaction = Transaction.objects.filter(user_id = request.user.id)
        page = request.GET.get('page', 1)
        paginator = Paginator(listtransaction, 10)
        try:
            listtransaction = paginator.page(page)
        except PageNotAnInteger:
            listtransaction = paginator.page(1)
        except EmptyPage:
            listtransaction = paginator.page(paginator.num_pages)
        return render(request, 'UserDashboard/transaction.html', context = {'listtransaction': listtransaction})

    

