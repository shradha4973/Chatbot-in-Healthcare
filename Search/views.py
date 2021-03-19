from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from Hospital.models import Doctor, Appointment, Report, Feedback, Transaction, Profile
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    doctor = get_data_queryset(query)
    context['doctor'] = doctor
    return render(request, 'Appointments/appointment.html',context={"doctor": doctor})

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        doctor = Doctor.objects.filter(Q(firstName__icontains=q) | Q(emailAddress__icontains=q) | Q(specialization__icontains=q))
        
        for doctor in doctor:
            queryset.append(doctor)
    
    return list(set(queryset)) 

def search_doctor(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    doctors = get_doctor(query)
    context['doctors'] = doctors
    page = request.GET.get('page', 1)
    paginator = Paginator(doctors, 10)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/admindashboard.html',context={"doctors": doctors})

def get_doctor(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        doctors = Doctor.objects.filter(Q(firstName__icontains=q) | Q(lastName__icontains=q) | Q(emailAddress__icontains=q) 
        | Q(specialization__icontains=q) | Q(qualification__icontains=q) | Q(date_created__icontains=q) | Q(appointment_price__icontains=q))
        
        for doctor in doctors:
            queryset.append(doctor)
    
    return list(set(queryset)) 

def search_user(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    user_list = get_user(query)
    context['user_list'] =  user_list
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/usertable.html',context={"user_list": user_list})

def get_user(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        profile = Profile.objects.all()
        user_list = User.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(username__icontains=q) | Q(email__icontains=q) | Q(profile__age__icontains=q) | Q(date_joined__icontains=q))
        for user in user_list:
            queryset.append(user)
    
    return list(set(queryset))  

def search_appointments(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    appointments = get_appointments(query)
    context['appointments'] =  appointments
    page = request.GET.get('page', 1)
    paginator = Paginator(appointments, 10)
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/listappointments.html',context={"appointments": appointments})

def get_appointments(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        appointments = Appointment.objects.filter(Q(user__id__icontains=q) | Q(appointment_date__icontains=q) | Q(appointment_time__icontains=q) | Q(doctor__firstName__icontains=q) | Q(doctor__doctor_id__icontains=q) | Q(doctor__specialization__icontains=q))
        for appointment in appointments:
            queryset.append(appointment)
    
    return list(set(queryset)) 


def search_feedbacks(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    feedback = get_feedback(query)
    context['feedback'] =  feedback
    page = request.GET.get('page', 1)
    paginator = Paginator(feedback, 10)
    try:
        feedback = paginator.page(page)
    except PageNotAnInteger:
        feedback = paginator.page(1)
    except EmptyPage:
        feedback = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/userfeedback.html',context={"feedback": feedback})

def get_feedback(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        feedback = Feedback.objects.filter(Q(user__id__icontains=q) | Q(feedback_date__icontains=q) | Q(user__username__icontains=q) | Q(user__email__icontains=q))
        for feedback in feedback:
            queryset.append(feedback)
    
    return list(set(queryset)) 


def search_transactions(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    transaction = get_transaction(query)
    context['transaction'] =  transaction
    page = request.GET.get('page', 1)
    paginator = Paginator(transaction, 10)
    try:
        transaction = paginator.page(page)
    except PageNotAnInteger:
        transaction = paginator.page(1)
    except EmptyPage:
        transaction = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/usertransaction.html', context={"transaction": transaction})

def get_transaction(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        transaction = Transaction.objects.filter(Q(user__id__icontains=q) | Q(doctor__doctor_id__icontains=q) | Q(date__icontains=q) | Q(price__icontains=q) |  Q(doctor__firstName__icontains=q) |  Q(doctor__lasttName__icontains=q))
        for transaction in transaction:
            queryset.append(transaction)
    
    return list(set(queryset)) 


def search_reports(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    reports = get_reports(query)
    context['reports'] =  reports
    page = request.GET.get('page', 1)
    paginator = Paginator(reports, 10)
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'AdminDashboard/usersreport.html', context={"reports": reports})

def get_reports(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        reports = Report.objects.filter(Q(user__username__icontains=q) | Q(doctor__firstName__icontains=q) | Q(doctor__specialization__icontains=q))
        for reports in reports:
            queryset.append(reports)
    
    return list(set(queryset)) 


def search_listtransactions(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    listtransaction = get_transaction(query)
    context['listtransaction'] =  listtransaction
    page = request.GET.get('page', 1)
    paginator = Paginator(listtransaction, 10)
    try:
        listtransaction = paginator.page(page)
    except PageNotAnInteger:
        listtransaction = paginator.page(1)
    except EmptyPage:
        listtransaction = paginator.page(paginator.num_pages)
    return render(request, 'UserDashboard/transaction.html', context={"listtransaction": listtransaction})

def get_transaction(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        listtransaction = Transaction.objects.filter(Q(user__id__icontains=q) | Q(doctor__doctor_id__icontains=q) | Q(date__icontains=q) | Q(price__icontains=q) |  Q(doctor__firstName__icontains=q))
        for listtransaction in listtransaction:
            queryset.append(listtransaction)
    
    return list(set(queryset)) 


def search_report(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    report = get_report(query)
    context['report'] =  report
    page = request.GET.get('page', 1)
    paginator = Paginator(report, 10)
    try:
        report = paginator.page(page)
    except PageNotAnInteger:
        report = paginator.page(1)
    except EmptyPage:
        report = paginator.page(paginator.num_pages)
    return render(request, 'UserDashboard/reports.html', context={"report": report})

def get_report(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        report = Report.objects.filter(Q(user__username__icontains=q) | Q(doctor__firstName__icontains=q) | Q(doctor__specialization__icontains=q))
        for report in report:
            queryset.append(report)
    
    return list(set(queryset)) 


def search_appointment(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET.get('q','').strip()	
    appointment = get_appointment(query)
    context['appointment'] =  appointment
    page = request.GET.get('page', 1)
    paginator = Paginator(appointment, 10)
    try:
        appointment = paginator.page(page)
    except PageNotAnInteger:
        appointment = paginator.page(1)
    except EmptyPage:
        appointment = paginator.page(paginator.num_pages)
    return render(request, 'UserDashboard/userappointment.html',context={"appointment": appointment})

def get_appointment(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        user = User.objects.all()
        doctor = Doctor.objects.all()
        appointment = Appointment.objects.filter(Q(user__id__icontains=q) | Q(appointment_date__icontains=q) | Q(appointment_time__icontains=q) | Q(doctor__firstName__icontains=q))
        for appointment in appointment:
            queryset.append(appointment)
    
    return list(set(queryset))



 
 
 