from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User
from sorl.thumbnail import ImageField
from taggit_autosuggest.managers import TaggableManager
from location_field.models.plain import PlainLocationField

# Create your models here.
class Event(models.Model):
	name = models.CharField('Nombre', max_length=200,unique=True)
	photo = ImageField('Foto',upload_to = 'eventos/')
	description = RichTextUploadingField('Descripción')
	init_date = models.DateField('Fecha de inicio')
	end_date  = models.DateField('Fecha de fin', blank=True,null=True)
	init_hour = models.TimeField('Hora de inicio')
	end_hour = models.TimeField('Hora de fin')
	reference_point = models.CharField('Punto de referencia', max_length=100)
	position = PlainLocationField(based_fields=['reference_point'], zoom=7,verbose_name='Posición')
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING,verbose_name='Organizador')
	tags = TaggableManager('Tags', help_text='Separar elementos con ","', blank=True)
	slug = models.SlugField(editable=False)

	class Meta:
		verbose_name_plural = 'Eventos'

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		return super(Evento,self).save(*args,*kwargs)


