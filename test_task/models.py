import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MyUser(models.Model): #, models.Model):
	"""Data class which describes users"""
	user = models.OneToOneField(User)
	cash = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
	ordered = models.PositiveIntegerField(default=0)
	completed = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.username


class Order(models.Model):
	"""Data class which describes orders"""
	title = models.CharField(max_length=200)
	price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	customer = models.ForeignKey(MyUser, related_name='+')
	performer = models.ForeignKey(MyUser, related_name='+')
	pub_date = models.DateTimeField('date published')
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.title