from django.contrib import admin
from .models import Donorextra, Ngoextra, Itemsdonated
# Register your models here.
admin.site.register(Ngoextra)
admin.site.register(Donorextra)
admin.site.register(Itemsdonated)