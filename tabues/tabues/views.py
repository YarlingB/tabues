from django.shortcuts import render
from django.db.models import Count
import datetime

from Blog.models import Blog
from Eventos.models import Event
from recursos_educativos.models import Educational_Resource

def index(request,template='index.html'):
	today = datetime.date.today()

	highlight_blogs = Blog.objects.annotate(cantity = Count('comment')).order_by('cantity')[:3]
	next_events = Event.objects.order_by('-init_date','init_hour')[:3]
	resources_list = Educational_Resource.objects.order_by('-id')[:10]
	return render(request,template,locals())
