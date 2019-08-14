from django.shortcuts import render
from Blog.models import *

# Create your views here.
def blogs(request, template= 'blog.html'):
	blogs_list = Blog.objects.order_by('-created_on')
	return render(request,template,locals())

def blog_detail(request,slug,template='blog_detalle.html'):
	object = Blog.objects.get(slug=slug);
	return render(request,template,locals())