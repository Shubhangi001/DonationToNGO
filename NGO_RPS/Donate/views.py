from django.shortcuts import render, redirect
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms, models
# from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.contrib.auth.models import Group
from .forms import NewDonorForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

def firstpage(request):
    return render(request,'Donate/firstpage.html')  

def donor_signup(request):
	if request.method == "POST":
		form = NewDonorForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("Donate:firstpage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return redirect("Donate:firstpage")
	form = NewDonorForm()
	return render (request=request, template_name="Donate/donor_signup.html", context={"NewDonorForm":NewDonorForm})

# def donor_login(request):
    

def donor_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("Donate:userprofile")
			# Redirect to a success page.
		else:
			messages.error(request, "Invalid information.")
			return redirect("Donate:donor_login")
	return render(request, "Donate/donor_login.html")

def ngo_signup(request):
    return render(request, "Donate/ngo_signup.html")

def ngo_login(request):
    return render(request, "Donate/ngo_login.html")
def userprofile(request):
    return render(request, "Donate/userprofile.html")



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
