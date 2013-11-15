import decimal

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

from test_task.models import MyUser, Order, TransAction
from test_task.forms import MyUserForm, OrderForm

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

class TransactionListView(ListView):
	template_name = 'test_task/transactions_list.html'
	context_object_name = 'transactions'

	def get_queryset(self):
		return TransAction.objects.filter(user=self.request.user)

class UserDetailView(DetailView):
	model = MyUser
	template_name = 'test_task/user.html'

#not very sure about this
#my view should be able to recognize logged in users
#to let them to perform the order
class OrderDetailView(DetailView):#, FormView):
	model = Order
	template_name = 'test_task/order.html'

	def post(self, request, pk):
		performer = self.request.user
		order = Order.objects.get(pk=pk)

		val = order.price * decimal.Decimal(0.95)

		performer.cash = performer.cash + val
		performer.completed += 1
		performer.save()

		order.performer = performer
		order.active = False
		order.save()

		ta = TransAction(user=performer, action="Performed order \'%s\'" % order.title, value=val)
		ta.save() 

		return HttpResponseRedirect('/')

class SignUpView(FormView):
	template_name = 'test_task/create_user.html'
	form_class = MyUserForm

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
	form_class = AuthenticationForm
	
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
	
	def form_valid(self, form):
		title = form.cleaned_data['title']
		price = form.cleaned_data['price']
		description = form.cleaned_data['description']
		pub_date = timezone.now()
		customer = self.request.user
		customer.ordered += 1
		customer.cash -= price
		customer.save()

		sys = MyUser.objects.get(pk=1)
		sys.cash += price * 0.05
		sys.save()

		transaction = TransAction(user=customer, action="Made order %s" % title, value=price)
		transaction.save()

		order = Order(title=title, price=price, description=description, pub_date=pub_date, customer=customer)
		order.save()

		return HttpResponseRedirect('/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')