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

def orders_index(request):
	orders = Order.objects.order_by('-price')
	context = {'orders': orders}
	return render(request, 'test_task/order_index.html', context)

class OrderIndexView(generic.ListView):
	template_name = 'test_task/order_index.html'
	context_object_name = 'orders'

	def get_queryset(self):
		return Order.objects.order_by('-price')

def user_detail(request, user_id):
	my_user = get_object_or_404(MyUser, pk=user_id)
	if my_user:
		logger.info("everything is fine")
	return render(request, 'test_task/user.html', {'user': my_user})

def order_detail(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	return render(request, 'test_task/order.html', {'order': order})

#This should be a class-based view
#This should be a sign-up view
def signup(request):
	if request.method == "GET":
		return HttpResponse("Get")
	if request.method == "POST":
		return HttpResponse("Post")