from django.urls import path
from .views import *

urlpatterns = [
	path('',blogs,name='blogs'),
	path('detalles/<slug>/',blog_detail,name='blog_detail'),
	path('agregar/respuesta/<id>/',add_answer, name='add_answer'),
]