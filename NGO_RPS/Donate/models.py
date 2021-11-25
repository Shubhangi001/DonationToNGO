from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class Ngoextra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobno = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    mail_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Donorextra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobno = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    mail_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

        
class Itemsdonated(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ngoname=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    description=models.CharField(max_length=400)
    quantity=models.IntegerField()
    pickup=models.CharField(max_length=200)

    def __str__(self):
        return self.type


# class Ngoextra(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     website = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     def __str__(self):
#         return self.ngoname
#     @property
#     def get_name(self):
#         return self.user.first_name
#     @property
#     def getuserid(self):
#         return self.user.id
