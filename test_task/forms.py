from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from test_task.models import MyUser

def validate_user(username):
	try:
		user = MyUser.objects.get(username=username)
	except ObjectDoesNotExist:
		return None
	raise ValidationError("Such user already exisis.")

class MyUserForm(forms.Form):
	username = forms.CharField(max_length=20, validators=[validate_user])
	password = forms.CharField(max_length=30)
	verify = forms.CharField(max_length=30)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	cash = forms.DecimalField()

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30)