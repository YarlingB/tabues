from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify


# Create your models here.

class Colaborador(models.Model):
	name = models.CharField('Nombre',max_length=200, unique=True)
	photo = ImageField()
	about = RichTextUploadingField(verbose_name='Descripción')
	slug = models.SlugField(max_length=200,editable=False)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return (Colaborador,self).save(*args,**kwargs)
		