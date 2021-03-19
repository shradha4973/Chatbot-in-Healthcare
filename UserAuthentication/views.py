from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models.functions import Length
from Hospital.models import Profile

def index(request):
    return redirect('/')

def register(request):
    first_name = ''
    last_name = ''
    username = ''
    password1= ''
    password2= ''
    email = ''
    age = ''
    profileImage = ''
    backgroundImage = ''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        age = request.POST['age']
        user_bio = request.POST['user_bio']
        userprofileImage = request.FILES.get('userprofileImage')
        userbackgroundImage = request.FILES.get('userbackgroundImage')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken')
                return redirect('register') 
            elif(len(username) <5 ):
                messages.error(request, 'Username must be of atleat 5 character')
                return redirect('register')

            elif(len(password1) < 8):
                messages.error(request, 'Password must be atleast of 8 character')
                return redirect('register')
                
            elif(len(age)>2):
                messages.error(request, 'Age must contain atmost 2 numeric value')
                return redirect('register')
            elif(int(age) < 1):
                messages.error(request,'Age must be positive number')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email address already in use')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username = username, password = password1, email = email)
                profile = Profile.objects.create(age = age, user_bio = user_bio, userprofileImage = userprofileImage, userbackgroundImage = userbackgroundImage, user = user)
                profile.save()
                return redirect('login_user')
        else:
            print('Password not matching')
            return redirect('register')
    else:
        return render(request, 'Accounts/register.html')
       

def login_user(request):
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,' Invalid credentials')
            return redirect('login_user')
    else:
        return render(request, 'Accounts/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')
    
