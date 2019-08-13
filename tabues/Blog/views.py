from django.shortcuts import render
from Blog.models import *

# Create your views here.
def blogs(request, template= 'index.html'):
	list_blogs = Blog.objects.order_by('-created_on')
	return render(request,template,locals())