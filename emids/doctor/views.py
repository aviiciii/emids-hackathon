from django.shortcuts import render
from db import models
# Create your views here.

def dash(request):
    # get the user
    username = request.user.get_username()
    # get the doctor
    doctor = models.Doctor.objects.get(id=username)
    
    # get the appointments
    appointments = models.Appointment.objects.filter(doctor=doctor, examination__isnull=True).all()


    # context
    context={
        'doctor':doctor,
        'appointments':appointments,
    }


    return render(request, 'login/index.html', context)


def patient_profile(request, patient_id):
    # get the user
    username = request.user.get_username()
    # get the doctor
    doctor = models.Doctor.objects.get(id=username)
    # get the patient
    patient = models.Patient.objects.get(id=patient_id)
    # get the appointments
    appointments = models.Appointment.objects.filter(patient=patient, doctor=doctor).all()
    # get the examinations
    examinations = models.Examination.objects.filter(appointment__in=appointments).all()
    # get the medicines
    medicines = models.Medicine.objects.all()

    # context
    context={
        'doctor':doctor,
        'patient':patient,
        'appointments':appointments,
        'examinations':examinations,
        'medicines':medicines,
    }

    return render(request, 'doctor/patient_profile.html', context)


def search(request, patient_id):
    # get the user
    username = request.user.get_username()
    # get the doctor
    doctor = models.Doctor.objects.get(id=username)
    # get the search term
    search_term = patient_id
    # get the patients
    patients = models.Patient.objects.filter(id__contains=search_term).all()

    # context
    context={
        'doctor':doctor,
        'patients':patients,
    }

    return render(request, 'doctor/search.html', context)