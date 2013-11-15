from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from test_task.models import MyUser

def validate_user_creation(username):
	try:
		user = MyUser.objects.get(username=username)
	except ObjectDoesNotExist:
		return None
	raise ValidationError("Such user already exisis.")

class MyUserForm(forms.Form):
	username = forms.CharField(max_length=20, validators=[validate_user_creation])
	password = forms.CharField(max_length=30)
	verify = forms.CharField(max_length=30)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	cash = forms.DecimalField(max_digits=20, decimal_places=2)

class OrderForm(forms.Form):
	title = forms.CharField(max_length=200)
	price = forms.DecimalField(max_digits=10, decimal_places=2)
	description = forms.CharField(widget=forms.Textarea)

class OrderPerformForm(forms.Form):
	pass