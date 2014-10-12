from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'blog.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^blogs/', include('blogs.urls', namespace="blogs")),
	url(r'^joeychapsblogs/', include('blogs.urls', namespace="blogs")),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^your-name/', include('blogs.urls', namespace="blogs")),
	(r'^comments/posted/$', 'blogs.views.comment_posted'),
	(r'^comments/', include('django.contrib.comments.urls')),
)
