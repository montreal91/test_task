from django.conf.urls import patterns, url

from test_task import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'users/(?P<user_id>\d+)', views.user_detail, name='user detail'),
	url(r'orders/(?P<order_id>\d+)', views.order_detail, name='order detail'),	
)