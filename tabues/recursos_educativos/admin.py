from django.contrib import admin
from .models import *

# EduFiles
class ArchivosInline(admin.TabularInline):
	model = EduFiles
	extra = 1

	

class ArchivoAdmin(admin.ModelAdmin):
	inlines = [ArchivosInline]

	def save_model(self,request,obj,form,change):
		obj.usuario = request.user
		obj.save()
		


# Register your models here.
admin.site.register(Thematic)
admin.site.register(Learning)
admin.site.register(Educational_Resource,ArchivoAdmin)

