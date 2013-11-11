import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	cash = models.FloatField(default=0)	
	is_customer = models.BooleanField(default=False)
	is_performer = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name


class Order(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	customer = models.ForeignKey(User)
	performer = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title