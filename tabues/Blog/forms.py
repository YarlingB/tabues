from django.db import models
from .models import Comment,Answer
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Comment
		exclude = ('blog','created_on','user')

class AnswerForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Answer
		exclude = ('comment','created_on','user')

		
			