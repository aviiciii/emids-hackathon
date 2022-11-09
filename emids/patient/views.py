from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'patient/dashboard.html')

def appointments(request, appointment_id):
    return render(request, 'patient/appointment.html')

def patient_report(request):
    return render(request, 'patient/patient_report.html')