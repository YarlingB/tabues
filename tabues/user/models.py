from django.db import models
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField

from colaborador.models import Colaborador

# Create your models here.

class User(AbstractUser):
	colaborador = models.ForeignKey(Colaborador, on_delete = models.CASCADE, null=True,blank=True)
	avatar = ImageField(upload_to='usuario/avatar',null=True,blank=True)

	def __str__(self):
		return self.username

	class Meta(object):
		unique_together = ('email',)
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		