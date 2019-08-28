from django.shortcuts import render
from .models import *
# Create your views here.
def colaborador(request,template='colaborador.html'):
	list_colaboradores = Colaborador.objects.order_by('-name')
	return render(request,template,locals())