from django.urls import path
from . import views
app_name='Donate'
urlpatterns = [
        path('', views.firstpage,name='firstpage'),
        path('donor', views.donor,name='donor'),
        path('ngo', views.ngo,name='ngo'),
        path('donor_signup', views.donor_signup,name='donor_signup'),
        path('donor_login', views.donor_login,name='donor_login'),
        path('ngo_signup', views.ngo_signup,name='ngo_signup'),
        path('ngo_login', views.ngo_login,name='ngo_login'),

]