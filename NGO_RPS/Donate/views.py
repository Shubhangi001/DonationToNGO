from django.shortcuts import render, redirect
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms
# from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.contrib.auth.models import Group,User
from .forms import DonationInfoForm, NewDonorForm, NewNGOForm, NGOExtraForm, DonorExtraForm, DonationInfoForm
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
	form1=NewNGOForm()
	form2=NGOExtraForm()
	mydict={'form1':form1,'form2':form2}
	if(request.method == "POST"):
		form1 = NewNGOForm(request.POST)
		form2 = NGOExtraForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			user = form1.save()
			user.set_password(user.password)
			user.save()
			f2=form2.save(commit=False)
			f2.user=user
			user2=f2.save()
			ngo_group = Group.objects.get_or_create(name='NGO')
			ngo_group[0].user_set.add(user)
		return HttpResponseRedirect('ngo_login')
	return render(request,"Donate/ngo_signup.html",context=mydict)

def donor_signup(request):
	form1 = NewDonorForm()
	form2 = DonorExtraForm()
	mydict={'form1':form1,'form2':form2}
	if(request.method == "POST"):
		form1 = NewDonorForm(request.POST)
		form2 = DonorExtraForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			user = form1.save()
			user.set_password(user.password)
			user.save()
			f2=form2.save(commit=False)
			f2.user=user
			user2=f2.save()
			donor_group = Group.objects.get_or_create(name='DONOR')
			donor_group[0].user_set.add(user)
		return HttpResponseRedirect('donor_login')
	return render(request,"Donate/donor_signup.html",context=mydict)


def afterlogin(request):
	if is_ngo(request.user):
		return HttpResponseRedirect('NGOprofile')		
	else:
		return HttpResponseRedirect('ngolist')

@login_required(login_url='donor_login')
def ngolist(request):
	ngos=models.Ngoextra.objects.all()
	return render(request,'Donate/ngolist.html',context={'ngos':ngos})
	

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
	# name=request.user.username
	# name=request.session['username']
	usr = models.Donorextra.objects.get(user_id=request.user.id)
	return render(request, "Donate/donorprofile.html",context={'usr':usr})

@login_required(login_url='ngo_login')
@user_passes_test(is_ngo)
def NGOprofile(request):
	ngo = models.Ngoextra.objects.get(user_id=request.user.id)
	return render(request, "Donate/NGOprofile.html",context={'ngo':ngo})

@login_required(login_url='donor_login')
def Item_sel(request):
	if(request.method == "POST"):
		name_of_ngo = request.POST.get('NGO_name')
	print(name_of_ngo)
	form=DonationInfoForm()
	if form.is_valid():
		pass
	mydict={'name_of_ngo':name_of_ngo,'form':form}
	# print(name_of_ngo)
	return render(request,"Donate/Item_sel.html",context=mydict)




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
