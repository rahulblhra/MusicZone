from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Song

class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False)
	last_name = forms.CharField(max_length=30,required=False)
	email = forms.EmailField(max_length=300,required=True,help_text='required')

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['title','audio']