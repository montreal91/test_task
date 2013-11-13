import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from test_task.models import MyUser, Order

#This logger is writing something somewhere but I can't read it in the terminal
logger = logging.getLogger('some name')

#This class is looking a little bit magical
class UserIndexView(generic.ListView):
	template_name = 'test_task/user_index.html'
	context_object_name = 'myuser_list'

	def get_queryset(self):
		return MyUser.objects.order_by('-cash')

class OrderIndexView(generic.ListView):
	template_name = 'test_task/order_index.html'
	context_object_name = 'orders'

	def get_queryset(self):
		return Order.objects.filter(active=True)

class UserDetailView(generic.DetailView):
	model = MyUser
	template_name = 'test_task/user.html'

#not very sure about this
#my view should be able to recognize logged in users
#to let them to perform the order
class OrderDetailView(generic.DetailView):
	model = Order
	template_name = 'test_task/order.html'

#Google-App-Engine style view
#class SignUpView(generic.View):
#	def get(self, request):
#		return render(request, 'test_task/sign_up.html')

#	def post(self, request):
#		return HttpResponse(request.POST['username'])

#It seems to me that that kind of magic doesn't work this time
class CreateMyUser(generic.edit.CreateView):
	model = MyUser
	fields = ['user', 'cash']