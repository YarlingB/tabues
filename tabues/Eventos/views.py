from django.shortcuts import render
from .models import *

# Create your views here.
def eventos(request,template='index.html'):
	return render(request,template,locals())