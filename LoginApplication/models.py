from django.db import models

# Create your models here.
class LoginDetails(models.Model):
    name = models.CharField(default='', max_length=20, help_text='Enter Yuur Name : ')
    email = models.EmailField(default='', max_length=25, help_text='Enter Valid Email Id')
    dob = models.DateField(default='YYYY-MM-DD', auto_now_add=False, help_text='Enter Date Of Birth')
    mobile = models.CharField(default='', max_length=12, help_text='Enter mobile Number')


    def __str__(self):
        return self.name
