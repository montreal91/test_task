from django.shortcuts import render
from django.http import HttpResponse
from test_task.models import UserUser

def index(request):
	userlist = UserUser.objects.order_by('last_name')
	output = ', '.join([p.last_name for p in userlist])
	return HttpResponse(output)

def user_detail(request, user_id):
	return HttpResponse("You're looking at user %s" % user_id)

def order_detail(request, order_id):
	return HttpResponse("You're looking at order %s" % order_id)