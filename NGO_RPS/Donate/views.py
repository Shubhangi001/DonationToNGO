from django.shortcuts import render, redirect
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.contrib.auth.models import Group
from .forms import NewDonorForm,NewNGOForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def firstpage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('afterlogin')
	return render(request,'Donate/firstpage.html')
def is_ngo(user):
    return user.groups.filter(name='NGO').exists()

def ngo_signup(request):
	form2=NewNGOForm()
	dict2={'form2':form2}
	if(request.method == "POST"):
		form2 = NewNGOForm(request.POST)
		if form2.is_valid():
			user = form2.save()
			user.set_password(user.password)
			user.save()
			ngo_group = Group.objects.get_or_create(name='NGO')
			ngo_group[0].user_set.add(user)
		return HttpResponseRedirect('ngo_login')
	return render(request,"Donate/ngo_signup.html",context=dict2)

def donor_signup(request):
	form = NewDonorForm()
	mydict={'form':form}
	if(request.method == "POST"):
		form = NewDonorForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			donor_group = Group.objects.get_or_create(name='DONOR')
			donor_group[0].user_set.add(user)
		return HttpResponseRedirect('donor_login')
	return render(request,"Donate/donor_signup.html",context=mydict)





def afterlogin(request):
	if is_ngo(request.user):
		return render(request,'Donate/ngo_afterlogin.html')
	else:
		return render(request,'Donate/userprofile.html')

# def donor_login(request):
    

# def donor_login(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect("Donate:userprofile")
# 		else:
# 			messages.error(request, "Invalid information.")
# 			return redirect("Donate:donor_login")
# 	return render(request, "Donate/donor_login.html")


def userprofile(request):
	
    return render(request, "Donate/userprofile.html")
def ngo_afterlogin(request):
    return render(request, "Donate/ngo_afterlogin.html")




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
