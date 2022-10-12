from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm, EditBlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
	"""Функция для представления домашней страницы"""
	post = BlogPost.objects.order_by('date_added')
	#text = post.get['id']
	context = {'post': post}
	return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
	if request.method != 'POST':
		form = BlogPostForm()
	else:
		form =BlogPostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect('blogs:index')
	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
	post = BlogPost.objects.get(id=post_id)
	if post.author != request.user:
		raise Http404
	if request.method != 'POST':
		form = EditBlogPostForm(instance=post)
	else:
		form =EditBlogPostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:index')
	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)

def error_not_in(request):
	return render(request, 'blogs/error_not_in.html')