from django.db import models
from recursos_educativos.models import Thematic
from user.models import User
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from taggit_autosuggest.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
	name = models.CharField('Nombre', max_length=250,unique=True)
	photo = ImageField('Imagen', upload_to='blogs/')
	created_on = models.DateField(auto_now_add=True)
	thematic = models.ForeignKey(Thematic, on_delete = models.DO_NOTHING,verbose_name='Temática')
	content = RichTextUploadingField('Contenido')
	tags = TaggableManager('Tags',help_text='Separe con "," cada elemento',blank=True)
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING,verbose_name='Autor')
	slug = models.SlugField(editable=False,max_length=250)

	class Meta:
		ordering = ['-created_on']		

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		return super(Blog,self).save(*args,*kwargs)

class Comment(models.Model):
	blog = models.ForeignKey(Blog,on_delete=models.CASCADE, verbose_name='Blog')
	content = RichTextUploadingField('Contenido')
	created_on = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='usuario')

	class Meta:
		verbose_name='Comentario'
		verbose_name_plural='Comentarios'

class Answer(models.Model):
	comment = models.ForeignKey(Comment,on_delete=models.CASCADE,verbose_name='Comentario')
	content = RichTextUploadingField('Contenido')
	created_on = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Usuario')

	class Meta:
		verbose_name='Respuesta'
		verbose_name_plural='Respuestas'
	
		
		



