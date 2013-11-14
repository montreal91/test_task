from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator

from test_task.models import MyUser, Order
from test_task.forms import MyUserForm, LoginForm, OrderForm

class UserIndexView(ListView):
	template_name = 'test_task/user_index.html'
	context_object_name = 'myuser_list'

	def get_queryset(self):
		"""Allows to show in the index page only active orders"""
		return MyUser.objects.order_by('-cash')

class OrderIndexView(ListView):
	template_name = 'test_task/order_index.html'
	context_object_name = 'orders'

	def get_queryset(self):
		return Order.objects.filter(active=True)

class UserDetailView(DetailView):
	model = MyUser
	template_name = 'test_task/user.html'

#not very sure about this
#my view should be able to recognize logged in users
#to let them to perform the order
class OrderDetailView(DetailView):
	model = Order
	template_name = 'test_task/order.html'

class SignUpView(FormView):
	template_name = 'test_task/create_user.html'
	form_class = MyUserForm
	success_url = '/'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		cash = form.cleaned_data['cash']

		new = MyUser.objects.create_user(username, email, password, 
			first_name=first_name, last_name=last_name, cash=cash)

		#bad style
		return HttpResponseRedirect('/login/')


class LogInView(FormView):
	template_name = 'test_task/login.html'
	form_class = LoginForm

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return HttpResponseRedirect('/')

class CreateOrderView(FormView):
	template_name = 'test_task/create_order.html'
	form_class = OrderForm
	
#	@method_decorator(login_required)
	def form_valid(self, form):
		title = form.cleaned_data['title']
		price = form.cleaned_data['price']
		description = form.cleaned_data['description']
		pub_date = timezone.now()
		customer = self.request.user

		order = Order(title=title, price=price, description=description, pub_date=pub_date, customer=customer)
		order.save()

		return HttpResponseRedirect('/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def la_view(request):
	if request.user.is_authenticated():
		return HttpResponse(request.user.username)
	else:
		return HttpResponse('Anonimous')