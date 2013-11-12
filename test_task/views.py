from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from test_task.models import MyUser, Order

def users_index(request):
	userlist = MyUser.objects.order_by('-cash')
	context = {'userlist': userlist}
	return render(request, 'test_task/user_index.html', context)

def orders_index(request):
	orders = Order.objects.order_by('-price')
	context = {'orders': orders}
	return render(request, 'test_task/order_index.html', context)

def user_detail(request, user_id):
	try:
		my_user = MyUser.objects.get(pk=user_id)
	except MyUser.DoesNotExist:
		raise Http404
	return render(request, 'test_task/user.html', {'user': my_user})

def order_detail(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	return render(request, 'test_task/order.html', {'order': order})