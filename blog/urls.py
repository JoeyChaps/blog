from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import os

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

	# (r'^home/joeychaps/Documents/blog/static/media/(.*)$', 'django.views.static.serve', {'document_root':           
	# 	os.path.join(os.path.dirname(__file__), 'static/media')}),
	
) 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
# 	urlpatterns += patterns('',
# 		url(r'^static/media/(?P<path>.*)$', 'django.views.static.serve', {
# 			'document_root': settings.MEDIA_ROOT, 
# 		}),
# 	)


# http://stackoverflow.com/questions/16196603/images-from-imagefield-in-django-dont-load-in-template
