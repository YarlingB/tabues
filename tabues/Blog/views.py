from django.shortcuts import render
from django.db.models import Count
from Blog.models import *
from recursos_educativos.models import Educational_Resource

# Create your views here.
def blogs(request, template= 'blog.html'):
	_blogs = Blog.objects.order_by('-created_on')
	blogs_list = _blogs.annotate(comm = Count('comment'))
	rs_list = Educational_Resource.objects.order_by('-id')[:3]

	return render(request,template,locals())

def blog_detail(request,slug,template='blog_detalle.html'):
	object = Blog.objects.get(slug=slug);
	_post = Blog.objects.filter(thematic = object.thematic.id).exclude(id=object.id).order_by('-created_on')
	related_post = _post.annotate(cantidad = Count('comment')).order_by('-cantidad')
	rs_list = Educational_Resource.objects.order_by('-id')[:3]
	return render(request,template,locals())