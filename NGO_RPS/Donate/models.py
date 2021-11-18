from django.db import models

class Ngolist(models.Model):
    ngoname = models.CharField(max_length=150)
    mobno = models.CharField(max_length=10)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.ngoname