from django.urls import path
from .views import *

urlpatterns = [
	path('',eventos,name='eventos'),
]