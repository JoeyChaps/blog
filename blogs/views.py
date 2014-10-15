from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from blogs.models import Post, Picture
from django.views import generic

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blogs/index.html', context)

class IndexView(generic.ListView):
	template_name = 'blogs/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):
		"""Return the last five published blogs."""
		return Post.objects.order_by('-pub_date')[:5]


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	pictures = post.picture_set.all()
	return render(request, 'blogs/detail.html', {'post': post, 'pictures': pictures})


class DetailView(generic.DetailView):
	model = Post
	template_name = 'blogs/detail.html'


def get_comment(request):
	# if this is a POST request, need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request ...
		form = CommentForm(request.POST)
		# check if it's valid
		if form.is_valid():
			# process the data in form.cleaned_data as required and redirect to a new URL
			return HttpResponseRedirect('/thanks/')

	# if a GET (or other method), create a blank form
	else:
		form = CommentForm()

	return render(request, 'blogs/comment.html', {'form': form})


def comment_posted(request):
	if request.GET['c']:
		comment_id, post_id = request.GET['c'].split(':')
		post = Post.objects.get(pk=post_id)

		if post:
			return HttpResponseRedirect(post.get_absolute_url())

	return HttpResponseRedirect("/")
