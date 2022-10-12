"""определение схем url для приложения blog"""

from django.urls import path #импорт функции path для связи URL с представлениями

from . import views #импорт функции views. '.'- точка указывает импортировать 
		#представления из каталога в котором находится текущий модуль url.py

app_name = 'blogs' #переменная помогает отличить этот файл url.py от 
		#одноименных файлов в других приложениях в проекте
urlpatterns = [
	#домашняя страница
	path('',views.index, name='index'),
	#страница создания нового поста
	path('new_post', views.new_post, name='new_post'),
	#страница редактирования поста
	path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
	#страница предупреждения о необходимости регистрации
	path('error_not_in/', views.error_not_in, name='error_not_in'),
]