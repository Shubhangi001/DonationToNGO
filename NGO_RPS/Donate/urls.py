from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name='Donate'
urlpatterns = [
        path('', views.firstpage,name='firstpage'),
        path('accounts/',include('django.contrib.auth.urls') ),
        path('userprofile', views.userprofile,name='userprofile'),
        path('donor_signup', views.donor_signup,name='donor_signup'),
        path('ngo_signup', views.ngo_signup,name='ngo_signup'),
        # path('donor_login', views.donor_login,name='donor_login'),
        path('logout', LogoutView.as_view(template_name='Donate/firstpage.html')),
        path('donor_login', LoginView.as_view(template_name='Donate/donor_login.html')),
        path('afterlogin', views.afterlogin),
        path('ngo_login', LoginView.as_view(template_name='Donate/ngo_login.html')),
        path('ngo_afterlogin', views.ngo_afterlogin,name='ngo_afterlogin'),

]