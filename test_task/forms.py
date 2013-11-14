from django import forms

class MyUserForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30)
	verify = forms.CharField(max_length=30)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	cash = forms.DecimalField()

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30)