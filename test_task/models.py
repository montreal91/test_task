import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser): 
	"""Data class which describes users"""
	cash = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
	ordered = models.PositiveIntegerField(default=0)
	completed = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('user detail', kwargs={'pk': self.pk})


class Order(models.Model):
	"""Data class which describes orders"""
	title = models.CharField(max_length=200)
	price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	customer = models.ForeignKey(MyUser, related_name='+', null=True)
	performer = models.ForeignKey(MyUser, related_name='+', null=True)
	pub_date = models.DateTimeField('date published')
	description = models.TextField(blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title