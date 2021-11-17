from django.urls import path
from . import views
app_name='Donate'
urlpatterns = [
        path('', views.firstpage,name='firstpage'),

  
]