from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
# homepage
def index(request):
    return render(request, 'login/index.html')

# patient login
def patient_login(request):
    if request.method=="POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
        user = authenticate(request, mobile=mobile, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('login')




    return render(request, 'login/patient_login.html')  

# doctor login 
def doctor_login(request):
    if request.method=="POST":
        mobile = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, username=id, password=password)
        #check if aunthentication successful
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Invalid id and/or password')
            return redirect('login')

    return render(request, 'login/login_doctor.html')
