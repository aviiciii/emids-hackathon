from django.shortcuts import render
from db import models
# Create your views here.

def dash(request):
    # get the user
    username = request.user.get_username()
    # get the doctor
    doctor = models.Doctor.objects.get(id=username)
    
    # get the appointments
    appointments = models.Appointment.objects.filter(doctor=doctor, )



    # context
    context={
        'doctor':doctor,
    }


    return render(request, 'login/index.html', context)
