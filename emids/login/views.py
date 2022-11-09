from django.shortcuts import render

# Create your views here.
# homepage
def index(request):
    return render(request, 'login/index.html')

# patient login
def patient_login(request):
    return render(request, 'login/patient_login.html')  

# doctor login 
def doctor_login(request):
    return render(request, 'login/doctor_login.html')
