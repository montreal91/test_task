from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('test_task.urls', namespace="task")),
    url(r'^admin/', include(admin.site.urls)),
)
