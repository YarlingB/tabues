from django.shortcuts import render
from .models import *
from Blog.models import Blog

# Create your views here.

def resources(request,template='recursos.html'):
	res_list = Educational_Resource.objects.order_by('-id')
	latest_blogs = Blog.objects.order_by('-created_on')[:3]
	return render(request,template,locals())

def resource_detail(request,slug,template='recursos_detalle.html'):
	# object = Educational_Resource.objects.get(slug=slug)
	return render(request,template,locals())