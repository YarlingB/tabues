from django.urls import path
from .views import *

urlpatterns = [
	path('info/',resources,name='resources'),
	path('info/detalles/<slug>/',resource_detail,name='resource_detail'),
	path('aprende/',learn,name='learn'),
	path('aprende/detalle/<slug>',learn_detail,name='learn_detail'),
]