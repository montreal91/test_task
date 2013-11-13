from django.conf.urls import patterns, url

from test_task import views

urlpatterns = patterns('',
	url(r'orders/(?P<pk>\d+)', views.OrderDetailView.as_view(), name='order detail'),
	url(r'^$|orders/', views.OrderIndexView.as_view(), name='order detail'), #matches '/' and 'orders/'
	url(r'users/(?P<pk>\d+)', views.UserDetailView.as_view(), name='user detail'),
	url(r'users/', views.UserIndexView.as_view(), name='users index'),
	url(r'signup/', views.signup, name='sign_up'),
)