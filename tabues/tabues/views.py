from django.shortcuts import render
from django.db.models import Count
import datetime

# from Blog.models import Blog
# from Eventos.models import Event

def index(request,template='index'):
	today = datetime.date.today()

	# highlight_blogs = Blog.objects.annotate(cantity = Count('comment')).order_by('cantity')[:3]
	# next_events = Event.objects.filter(init_date__gte=today).order_by('-init_date','init_hour')[:3]
	return render(request,template,locals())
