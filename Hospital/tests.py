from django.test import TestCase
from django.contrib.auth.models import User
from . models import Profile, Transaction, Feedback, Appointment, Doctor
from datetime import date

class ModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name= 'Shraddha', last_name='Subba', username = 'shraddha123', password = 'coursework', email = 'np03a180039@heraldcollege.edu.np')
        self.doctor = Doctor.objects.create(firstName = 'Smeena', lastName = 'Shrestha', emailAddress = 'smeena@gmail.com', specialization = 'Main surgeon',  qualification = 'M.D.', appointment_price = 800, profileImage = "static/images/image-2.png", backgroundImage ="static/images/image-2.png")
        self.profile = Profile.objects.create(age = 10, user_bio = 'Dream with passion for now', userprofileImage = "static/images/image-2.png", userbackgroundImage = "static/images/image-2.png", user = self.user)
        self.appointment = Appointment.objects.create(appointment_date = "2020-11-22", appointment_time = "13:16", message = "I want an appointment fpr my checkup", user = self.user, doctor = self.doctor)
        self.feedback = Feedback.objects.create(feedback = "I like the service provided by medicare.", user = self.user, profile = self.user.profile)
        self.transaction = Transaction.objects.create(price = 800 , user = self.user, doctor = self.doctor, appointment = self.appointment)
        
    
    def testUser(self):
        userinfo = User.objects.get(username = "shraddha123")
        self.assertEqual(userinfo.username, "shraddha123")

    def testProfile(self):
        userprofile = Profile.objects.get(user_bio = "Dream with passion for now")
        self.assertEqual(userprofile.user_bio, "Dream with passion for now")
    
    def testAppointment(self):
        userappointment = Appointment.objects.get(user_id = self.user.id)
        self.assertEqual(userappointment.appointment_date, date(2020,11,22))
    
    def testFeedback(self):
        userfeedback = Feedback.objects.get(user_id = self.user.id)
        self.assertEqual(userfeedback.feedback, "I like the service provided by medicare.")
    
    def testTransaction(self):
        usertransaction = Transaction.objects.get(doctor_id = self.doctor.doctor_id)
        self.assertEqual(usertransaction.price, 800)