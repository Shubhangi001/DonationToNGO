from django.shortcuts import render, redirect
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.contrib.auth.models import Group,User
from .forms import NewDonorForm,NewNGOForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# from NGO_RPS import Donate


def firstpage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('afterlogin')
	return render(request,'Donate/firstpage.html')
def is_ngo(user):
    return user.groups.filter(name='NGO').exists()
def home(request):
	return render(request,'Donate/firstpage.html')


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
	ngos=models.Ngolist.objects.all()
	if is_ngo(request.user):
		return render(request,'Donate/NGOprofile.html')
	else:
		return render(request,'Donate/ngolist.html',context={'ngos':ngos})
@login_required(login_url='ngo_login')
def ngolist(request):
	ngos=models.Ngolist.objects.all()
	return render(request,'Donate/ngolist.html',context={'ngos':ngos})
	




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

@login_required(login_url='donor_login')
def donorprofile(request):
	# usr = User.objects.get(username=username)
	return render(request, "Donate/donorprofile.html")

@login_required(login_url='ngo_login')
@user_passes_test(is_ngo)
def ngo_afterlogin(request):
    return render(request, "Donate/ngo_afterlogin.html")

@login_required(login_url='donor_login')
def Item_sel(request):
	return render(request,"Donate/Item_sel.html")




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
