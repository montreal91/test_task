import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserUser(User):
	cash = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)	

	def __unicode__(self):
		return self.username


class Order(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	customer = models.ForeignKey(UserUser, related_name='+')
	performer = models.ForeignKey(UserUser, related_name='+')
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title