from django.shortcuts import render
from .models import *
from Blog.models import Blog
from recursos_educativos.models import Educational_Resource

# Create your views here.
def events(request,template='eventos.html'):
	event_list = Event.objects.order_by('-id')
	highlight_blogs = Blog.objects.order_by('-id')
	last_rs = Educational_Resource.objects.order_by('-id')[:3]
	return render(request,template,locals())

def event_detail(request,slug,template='evento_detalle.html'):
	object = Event.objects.get(slug=slug)
	return render(request,template,locals())