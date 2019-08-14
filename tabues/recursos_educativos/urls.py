from django.urls import path
from .views import *

urlpatterns = [
	path('',resources,name='resources'),
	path('detalles/<slug>/',resource_detail,name='resource_detail'),
]