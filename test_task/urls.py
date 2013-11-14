from django.conf.urls import patterns, url

from test_task import views

urlpatterns = patterns('',
	url(r'orders/(?P<pk>\d+)', views.OrderDetailView.as_view(), name='order detail'),
	url(r'^$|orders/', views.OrderIndexView.as_view(), name='order detail'), #matches '/' and 'orders/'
	url(r'users/(?P<pk>\d+)', views.UserDetailView.as_view(), name='user detail'),
	url(r'users/signup', views.SignUpView.as_view(), name='sign_up'),
	url(r'users/login', views.LogInView.as_view(), name='log_in'),
	url(r'users/logout', views.logout_view, name='log_out'),
	url(r'users/', views.UserIndexView.as_view(), name='users index'),
)