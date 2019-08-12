from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from user.models import User

# Create your models here.
class Thematic(models.Model):
	name = models.CharField(max_length=200, unique=True)

	class Meta:
		verbose_name_plural = 'Temas'
		verbose_name = 'Tema'

	def __str__(self):
		return self.name					

class Learning(models.Model):
	tittle = models.CharField('Título', max_length=200)
	photo = ImageField('Foto',upload_to='aprende/')
	content = RichTextUploadingField(verbose_name='Contenido')
	thematic = models.ForeignKey(Thematic, on_delete = models.DO_NOTHING)
	created_on = models.DateField('Fecha de creación', auto_now_add=True)
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	class Meta:
		verbose_name='Aprende'
		verbose_name_plural='Aprende'

	def __str__(self):
		return self.tittle
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Learning,self).save(*args,*kwargs)
	 
class Educational_Resource(models.Model):
	tittle = models.CharField('Título',max_length=200)
	photo = ImageField('Foto',upload_to='recursos-educativos/')
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)


	class Meta:
		verbose_name='Recurso educativo'
		verbose_name_plural='Recursos educativos'

	def __str__(self):
		return self.tittle

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Educational_Resource,self).save(*args,*kwargs)
	 		 


