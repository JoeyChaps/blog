from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from blogs.models import Entry, Picture
from django.views import generic


class IndexView(generic.ListView):
	template_name = 'blogs/index.html'
	context_object_name = 'latest_entry_list'

	def get_queryset(self):
		"""Return the last five published blogs."""
		return Entry.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Entry
	template_name = 'blogs/detail.html'

def index(request):
	latest_entry_list = Entry.objects.order_by('-pub_date')[:5]
	context = {'latest_entry_list': latest_entry_list}
	return render(request, 'blogs/index.html', context)

def detail(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)
	pictures = entry.picture_set.all()
	return render(request, 'blogs/detail.html', {'entry': entry, 'pictures': pictures})

def home(request):
	return render(request, 'blogs/home.html')

def about(request):
	return render(request, 'blogs/about.html')

def comment_posted(request):
	if request.GET['c']:
		return HttpResponseRedirect(request.META['HTTP_REFERER'])

	return HttpResponseRedirect("/")
