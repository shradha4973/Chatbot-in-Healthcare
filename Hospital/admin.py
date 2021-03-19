from django.contrib import admin
from . models import Doctor, Profile, Appointment, Feedback, Report

admin.site.register(Doctor)
admin.site.register(Profile)
admin.site.register(Appointment)
admin.site.register(Feedback)
admin.site.register(Report)


