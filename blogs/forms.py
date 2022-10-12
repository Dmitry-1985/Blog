from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	"""Создание формы для добавления тем"""
	class Meta:
		model = BlogPost
		fields = ['title', 'text']
		labels = {'title':'Название темы', 'text':'Текст'}

class EditBlogPostForm(forms.ModelForm):
	"""Форма для редактирования текста постов"""
	class Meta:
		model = BlogPost
		fields = ['text']
		labels = {'text':'Редактирование текста'}