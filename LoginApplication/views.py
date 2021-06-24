from django.core.checks.messages import Error
from django.shortcuts import render
from datetime import date, datetime
from django.http import HttpResponse
from .models import LoginDetails
from .validators import *
# Create your views here.


def home(request):
    #print(request.POST)
    if request.method == 'POST':
        
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('dob') and request.POST.get('mobile'):
            #data = LoginDetails(request.POST)
            name = request.POST.get('name')
            email = request.POST.get('email')
            dob = request.POST.get('dob') 
            mobile = request.POST.get('mobile')
            print(dob)
            print(email)
            if not dataValidateMobile(mobile) :
                return render(request, 'registration.html', {'Mobile_error_message':"Invalid Mobile Number"})
            if not dataValidatorName(name):
                return render(request, 'registration.html', {'Name_error_message':"invalid Name"})
            if not dataValidateAge(dob):
                return render(request, 'registration.html', {'Dob_error_message':"Age should be Greater than 18"})
            else:
                LoginDetails.objects.create(name=name, email=email, dob=dob, mobile=mobile)
            
            

    else:
        return render(request, 'registration.html')
        #return render(request, 'registration.html', {'error_message':""})

    return render(request, 'registration.html')
    

def insert(request):
    pass

