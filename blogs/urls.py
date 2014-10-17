from django.conf.urls import patterns, url, include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blogs import views

urlpatterns = patterns('', 
	# ex: /blogs/
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),

	# url(r'^$', views.HomeView.as_view(), name='home'),

	# ex: /blogs/5/
	url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
	# url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)

# urlpatterns += staticfiles_urlpatterns()