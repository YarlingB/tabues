from django.urls import path
from .views import *

urlpatterns = [
	path('',events,name='eventos'),
	path('detalles/<slug>/',event_detail,name='event_detail'),

]