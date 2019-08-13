from django.shortcuts import render
from .models import *
# Create your views here.
def colaborador(request,template=''):
	return render(request,template,locals())