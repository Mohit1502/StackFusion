from datetime import datetime, date

from django.core.mail import send_mail
from django.http import request


def dataValidatorName(names):
    length=0
    for char in names:
        if char.isalpha():
            length += 1
            
    if(length == len(names) and len(names)<=10): 
        print('Valid Name')
        return True
    else: 
        print('Invalid Name')
        return False

# To validate Correct Mobile number
def dataValidateMobile(number):
    if (number.isdigit() and len(number)==10): 
        print('Valid Mobile Nuber') 
        return True
    else: 
        print('Invalid Mobile Number !')
        return False

def dataValidateAge(born):
    today = date.today() 
    born = datetime.strptime(born, '%Y-%m-%d').date()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    print(age)
    if age>=18:
        return True
    else:
        return False


# To send mail function
# email_id = request.POST.get('email')

# send_mail(
#     'Dummy Mail',
#     'Hello Everybody! I hope this mail finds you in well and safe.',
#     '2019mohitkumar.tiwari@ves.ac.in',
#     ['email_id'],
#     fail_silently=False,
# )