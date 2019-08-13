from django.shortcuts import render
from .models import *

# Create your views here.

def resources(request,template=''):
	res_list = Educational_Resource.objects.order_by('')
	return render(request,template,locals())