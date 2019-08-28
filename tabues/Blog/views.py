from django.shortcuts import render,redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

from recursos_educativos.models import Educational_Resource

# Create your views here.
def blogs(request, template= 'blog.html'):
	_blogs = Blog.objects.order_by('-created_on')
	blogs_list = _blogs.annotate(comm = Count('comment'))
	rs_list = Educational_Resource.objects.order_by('-id')[:3]

	return render(request,template,locals())

def blog_detail(request,slug,template='blog_detalle.html'):
	object = Blog.objects.get(slug=slug)
	# _post = Blog.objects.filter(thematic = object.thematic.id).order_by('-created_on')
	related_post = Blog.objects.filter(thematic = object.thematic.id).annotate(cantidad = Count('comment')).order_by('-cantidad')
	rs_list = Educational_Resource.objects.order_by('-id')[:3]

	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			b_comment = form.save(commit=False)
			b_comment.blog = object
			b_comment.user = request.user
			b_comment.save()
			form = CommentForm()

	else:

		form = CommentForm()
	return render(request,template,locals())

@login_required
def add_answer(request,id,template='add_answer.html'):
	object = Comment.objects.get(id=id)
	if request.method == 'POST':
		form = AnswerForm(request.POST, request.FILES)
		if form.is_valid():
			a_comment = form.save(commit=False)
			a_comment.comment = object
			a_comment.user = request.user
			a_comment.save()
	else:
		form = AnswerForm()
	return render(request,template,locals())

@login_required
def edit_answer(request,id,template='editar_respuesta.html'):
	object = Answer.objects.get(id=id)
	if request.method == 'POST':
		print ("Method post")
		form = AnswerForm(request.POST, request.FILES,instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.save()
			# return redirect('blog_detail', slug=object.comment.blog.slug)
	else:
		form = AnswerForm(instance=object)

	return render(request,template,locals())


@login_required
def edit_comment(request,id,template='editar_comentario.html'):
	object = Comment.objects.get(id=id)
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES,instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.save()

			return redirect('blog_detail', slug=object.Blog.slug)
	else:
		form = CommentForm(instance=object)
	return render(request,template,locals())

@login_required
def delete_answer(request,id):
	ans = Answer.objects.get(id=id)
	ans_slug = ans.comment.blog.slug
	ans.delete()

	return redirect('blog_detail', slug=ans_slug)

@login_required
def delete_comment(request,id):
	comm = Comment.objects.get(id=id)
	slug_comment = comm.blog.slug
	comm.delete()

	return redirect('blog_detail', slug=slug_comment)



