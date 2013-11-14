import utils

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.views import generic

from django.contrib.auth.models import User
from test_task.models import MyUser, Order

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
		
		try:
			cash = float(request.POST['cash'])
		except ValueError:
			cash = 0.0

		any_error = False
		context = {'username': username, 'email': email, 'first_name': f_name, 'last_name': l_name, 
			'cash': cash}

		if not utils.valid_username(username):
			context['error_username'] = "That's not a valid username."
			any_error = True

		if not utils.valid_password(password):
			context['error_password'] = "That's not a valid password."
			any_error = True

		if password != verify:
			context['error_verify'] = "Your passwords didn't match."
			any_error = True

		if not utils.valid_email(email):
			context['error_email'] = "That's not a valid e-mail."
			any_error = True

		if any_error:
			return render(request, 'test_task/myuser_form.html', context)

		else:
			try:
				new_user = User.objects.create_user(username, email, password)
			except IntegrityError:
				context['error_username'] = "Such user is already exists."
				return render(request, 'test_task/myuser_form.html', context)

			new_user.first_name = f_name
			new_user.last_name = l_name
			new_user.save()
			new_myuser = MyUser(user=u, cash=cash)
			new_myuser.save()
			response = HttpResponseRedirect('/users/%s' % m.pk)
			response.set_cookie('cookies', '%s' % m.pk)
			return response