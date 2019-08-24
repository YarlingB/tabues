from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from user.models import User

# Create your models here.
info_type=(
	(1,'ETS'),
	(2,'Embarazo')
)
class Thematic(models.Model):
	name = models.CharField('Nombre',max_length=200, unique=True)

	class Meta:
		verbose_name_plural = 'Temas'
		verbose_name = 'Tema'

	def __str__(self):
		return self.name					

class Learning(models.Model):
	tittle = models.CharField('Título', max_length=200)
	photo = ImageField('Foto',upload_to='recursos-educativos/aprende')
	info_type = models.PositiveSmallIntegerField('Categoría',choices=info_type)	
	content = RichTextUploadingField(verbose_name='Contenido')
	thematic = models.ForeignKey(Thematic, on_delete = models.DO_NOTHING,verbose_name='Temática')
	created_on = models.DateField('Fecha de creación', auto_now_add=True)
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='Autor')

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
	photo = ImageField('Foto',upload_to='recursos-educativos/',blank=True)
	info_type = models.PositiveSmallIntegerField('Categoría',choices=info_type)
	thematic = models.ForeignKey(Thematic, on_delete = models.DO_NOTHING,verbose_name='Temática')
	content = RichTextUploadingField(verbose_name='Contenido')
	created_on = models.DateField('Fecha de creación', auto_now_add=True)
	slug = models.SlugField(max_length=200, editable=False)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='Autor')


	class Meta:
		verbose_name='Recurso educativo'
		verbose_name_plural='Recursos educativos'

	def __str__(self):
		return self.tittle

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		return super(Educational_Resource,self).save(*args,*kwargs)

class EduFiles(models.Model):
	publication = models.ForeignKey(Educational_Resource,on_delete=models.CASCADE,verbose_name='Archivo')
	nombre = models.CharField(max_length=350)
	archivo_pdf = models.FileField(upload_to='recursos-educativos/archivos/')

	def __str__(self):
		return u'%s' % self.publication

	class Meta:
		verbose_name_plural = 'Archivos'
		
	 		 


