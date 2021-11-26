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
    types=(
		('books',"Books"),
		('medicines',"Medicines"),
		('clothes',"Clothes"),
		('food',"Food"),
	)
    stats=(
        ('pickup confirmed','Pickup confirmed'),
        ('picked up','Picked up'),
        ('delivered','Delivered'),
        ('NA','NA'),

    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ngoname=models.ForeignKey(Ngoextra,on_delete=models.CASCADE,null=True)
    # ngoname=models.CharField(max_length=10,blank=True)
    type=models.CharField(max_length=10,choices=types)
    description=models.CharField(max_length=400)
    quantity=models.IntegerField()
    pickup=models.CharField(max_length=200)
    status=models.CharField(max_length=20,choices=stats,default='NA')

    # def __str__(self/


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
