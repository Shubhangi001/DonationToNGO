from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# from . import models
class NewNGOForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','password']


class NewDonorForm(forms.ModelForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields=['first_name','last_name','username','password']


	# def save(self, commit=True):
	# 	user = super(NewDonorForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user