from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import Feedback, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def services(request, pk):
    feedback = Feedback.objects.all()
    if User.objects.filter(pk = request.user.id):
        user = User.objects.get(pk = request.user.id)
        profile = Profile.objects.filter(pk= request.user.id)
        if request.method == 'POST':
            try:
                feedback = request.POST['feedback']
                feedback = Feedback.objects.create(feedback = feedback, user = user, profile = user.profile)
                feedback.save()
                messages.success(request, 'Thank You for sending your feedback')
                return redirect('services', pk = user.id)  
            except Exception as exp:
                res = ('You have already send us your feedback') 
                messages.error(request,res)
                return redirect('services', pk = user.id)                            
        else:
            return render(request, "Services/services.html", context = {'feedback': feedback})       
    else:
        messages.error(request, 'No feedback found')
        return render(request, "Services/services.html", context = {'feedback': feedback})




 


