import logging
import utils

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.models import User
from test_task.models import MyUser, Order

#This logger is writing something somewhere but I can't read it in the terminal
logger = logging.getLogger('some name')

#This class is looking a little bit magical
class UserIndexView(generic.ListView):
	template_name = 'test_task/user_index.html'
	context_object_name = 'myuser_list'

	def get_queryset(self):
		"""Allows to show in the index page only active orders"""
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
#This looks ugly
class SignUpView(generic.View):
	def get(self, request):
		return render(request, 'test_task/myuser_form.html')

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		verify = request.POST['verify']
		email = request.POST['email']
		f_name = request.POST['first_name']
		l_name = request.POST['last_name']

		any_error = False
		error_username, error_password, error_verify, error_email = '', '', '', ''

		if not utils.valid_username(username):
			error_username = "That's not a valid username."
			any_error = True

		if not utils.valid_password(password):
			error_password = "That's not a valid password."
			any_error = True

		if password != verify:
			error_verify = "Your passwords didn't match."
			any_error = True

		if not utils.valid_email(email):
			error_email = "That's not a valid e-mail."
			any_error = True

		if any_error:
			context = {
				'username': username,
				'email': email,
				'first_name': f_name,
				'last_name': l_name,
				'error_username': error_username,
				'error_verify': error_verify,
				'error_password': error_password,
				'error_email': error_email
			}
			return render(request, 'test_task/myuser_form.html', context)

		else:
			u = User.objects.create_user(username, email, password)
			u.first_name = f_name
			u.last_name = last_name
			u.save()
			m = MyUser(user=u, cash=cash)
			m.save()
			return HttpResponse(m.pk)