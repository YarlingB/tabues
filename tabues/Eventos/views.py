from django.shortcuts import render
from .models import *

# Create your views here.
def events(request,template='index.html'):
	event_list = Event.objects.order_by('-init_date')
	return render(request,template,locals())

def event_detail(request,slug,template='evento_detalle.html'):
	object = Event.objects.get(slug=slug)
	return render(request,template,locals())