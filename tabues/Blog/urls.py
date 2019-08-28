from django.urls import path
from .views import *

urlpatterns = [
	path('',blogs,name='blogs'),
	path('detalles/<slug>/',blog_detail,name='blog_detail'),
	path('agregar/respuesta/<id>/',add_answer, name='add_answer'),
	path('editar/respuesta/<id>',edit_answer,name='edit_answer'),
	path('eliminar/respuesta/<id>',delete_answer,name='delete_answer'),
	path('editar/comentario/<id>/',edit_comment,name='edit_comment'),
	path('eliminar/comentario/<id>/',delete_comment,name='delete_comment'),
]