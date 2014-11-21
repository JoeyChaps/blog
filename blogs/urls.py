from django.conf.urls import patterns, url, include
from blogs import views

urlpatterns = patterns('', 
	# ex: /blogs/
	url(r'^$', views.IndexView.as_view(), name='index'),

	url(r'^(?P<entry_id>\d+)/$', views.detail, name='detail'),
)
