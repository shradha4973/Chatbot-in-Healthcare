from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    user_amount = models.IntegerField(default=0)
    user_bio = models.TextField(max_length = 1000, null = True)
    userprofileImage = models.ImageField(upload_to = 'picture',)
    userbackgroundImage = models.ImageField(upload_to = 'picture', default = 'static/images/blank-white-page.jpg')
    
    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length = 50, default= False)
    lastName = models.CharField(max_length = 50, default = False)
    emailAddress = models.EmailField(max_length = 100)
    specialization = models.CharField(max_length = 500) 
    qualification = models.CharField(max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)
    appointment_price = models.IntegerField(default = 0)
    profileImage = models.ImageField(upload_to = 'picture', null = True)
    backgroundImage = models.ImageField(upload_to = 'picture', null = True)
  
    def __str__(self):
        return self.firstName

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key = True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)

class Feedback(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE)
    feedback = models.TextField(max_length = 200, blank = True)
    feedback_date = models.DateField(auto_now_add= True)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete = models.CASCADE)
    report_date = models.DateField(auto_now = True)
    report_pdf = models.FileField(upload_to = 'reports/')
    report_description = models.TextField(max_length = 300, blank = True)
   
class Transaction(models.Model):
    price = models.IntegerField(null = False)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    


    



