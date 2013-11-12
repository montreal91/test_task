from django.conf.urls import patterns, url

from test_task import views

urlpatterns = patterns('',
	url(r'^$', views.UserIndexView.as_view(), name='users index'),
	url(r'users/(?P<user_id>\d+)', views.user_detail, name='user detail'),
	url(r'orders/(?P<order_id>\d+)', views.order_detail, name='order detail'),	
	url(r'orders/', views.OrderIndexView.as_view(), name='order detail'),
	url(r'signup/', views.signup, name='sign_up'),
)