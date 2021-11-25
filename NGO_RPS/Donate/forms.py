from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# from . import models
class NewNGOForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','password']

class NGOExtraForm(forms.ModelForm):
    class Meta:
        model=models.Ngoextra
        fields=['mobno', 'place', 'website', 'mail_id']

class NewDonorForm(forms.ModelForm):
	# email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields=['first_name','last_name','username','password']

class DonorExtraForm(forms.ModelForm):
	class Meta:
		model = models.Donorextra
		fields=['mobno', 'telephone', 'address', 'mail_id']

# class DonationInfoForm(forms.ModelForm):
# 	class Meta:
# 		model = models.Itemsdonated
# 		fields=['ngoname', 'type', 'description', 'quantity','pickup']


	# def save(self, commit=True):
	# 	user = super(NewDonorForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user