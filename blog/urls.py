from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import os
from blogs import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^blogs/', include('blogs.urls', namespace="blogs")),
	url(r'^joeychapsblogs/', include('blogs.urls', namespace="blogs")),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', views.home, name='home'),
	url(r'^about/', views.about, name='about'),
	(r'^comments/', include('django.contrib.comments.urls')),
) 
