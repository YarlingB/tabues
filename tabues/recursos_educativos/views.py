from django.shortcuts import render
from .models import *

# Create your views here.

def resources(request,template='index.html'):
	res_list = Educational_Resource.objects.order_by('')
	return render(request,template,locals())

def resource_detail(request,slug,template='index.html'):
	object = Educational_Resource.objects.get(slug=slug)
	return render(request,template,locals())