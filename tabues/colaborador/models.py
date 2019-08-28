from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify


# Create your models here.
class TipoColaborador(models.Model):
	name_colaborador = models.CharField('Nombre',max_length=250,unique=True)

	def __str__(self):
		return self.name_colaborador
		
	class Meta:
		verbose_name='Tipo de Colaborador'
		verbose_name_plural = "Tipos de Colaboradores"
		 		 
		
class Colaborador(models.Model):
	name = models.CharField('Nombre',max_length=200, unique=True)
	photo = ImageField()
	tipo = models.ForeignKey(TipoColaborador, on_delete=models.CASCADE,verbose_name='Tipo de Colaborador')
	about = RichTextUploadingField(verbose_name='Descripción')
	slug = models.SlugField(max_length=200,editable=False)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Colaborador,self).save(*args,**kwargs)
		