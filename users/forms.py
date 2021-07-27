from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	class Meta:
		model = User  # affected model
		fields = ['username', 'email', 'password1', 'password2']  # the fields needed in form


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()


	class Meta:
		model = User  # affected model
		fields = ['username', 'email']  # the fields needed in form


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'quote', 'fb_link', 'linkedin_link', 'twitter_link', 'insta_link', 'image']
		labels = {
			'bio': ('Bio'),
			'quote': ('Motivation'),
            'fb_link': ('FB'),
            'linkedin_link': ('in'),
            'twitter_link': ('TW'),
            'insta_link': ('IN'),
        }
