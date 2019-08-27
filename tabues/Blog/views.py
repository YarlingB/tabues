from django.shortcuts import render
from django.db.models import Count
from .models import *
from .forms import *

from recursos_educativos.models import Educational_Resource

# Create your views here.
def blogs(request, template= 'blog.html'):
	_blogs = Blog.objects.order_by('-created_on')
	blogs_list = _blogs.annotate(comm = Count('comment'))
	rs_list = Educational_Resource.objects.order_by('-id')[:3]

	return render(request,template,locals())

def blog_detail(request,slug,template='blog_detalle.html'):
	object = Blog.objects.get(slug=slug)
	# _post = Blog.objects.filter(thematic = object.thematic.id).order_by('-created_on')
	related_post = Blog.objects.filter(thematic = object.thematic.id).annotate(cantidad = Count('comment')).order_by('-cantidad')
	rs_list = Educational_Resource.objects.order_by('-id')[:3]

	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			b_comment = form.save(commit=False)
			b_comment.blog = object
			b_comment.user = request.user
			b_comment.save()
			form = CommentForm()

	else:
		form = CommentForm()
	return render(request,template,locals())


def add_answer(request,id,template='add_answer'):
	if reques.method == 'POST':
		
	return render(request,template,locals())