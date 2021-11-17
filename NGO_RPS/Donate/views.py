from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.contrib.auth.models import Group


# Create your views here.
def firstpage(request):
    return render(request,'Donate/firstpage.html') 

def donor(request):
    return render(request,'Donate/donor.html') 

def ngo(request):
    return render(request,'Donate/ngo.html') 

def donor_signup(request):
    return render(request, "Donate/donor_signup.html")

def donor_login(request):
    return render(request, "Donate/donor_login.html")

def ngo_signup(request):
    return render(request, "Donate/ngo_signup.html")

def ngo_login(request):
    return render(request, "Donate/ngo_login.html")


# def adminsignup_view(request):
#     form=forms.AdminSigupForm()
#     if request.method=='POST':
#         form=forms.AdminSigupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
#             my_admin_group = Group.objects.get_or_create(name='NGO')
#             my_admin_group[0].user_set.add(user)
#             return HttpResponseRedirect('adminlogin')
#     return render(request,'library/adminsignup.html',{'form':form})
