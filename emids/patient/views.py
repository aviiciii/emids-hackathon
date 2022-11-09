from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'patient/dashboard.html')

def search(request):
    return render(request, 'patient/search.html')

def patient_profile(request):
    return render(request, 'patient/patient_profile.html')