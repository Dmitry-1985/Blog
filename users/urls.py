"""Определяет схемы URL для пользователей"""

from django.urls import path, include
	#include - функция для включения аутентификационных URL-адресов по умолчанию, 
                                                                    #определенных Django
    #эти URL-адреса по умолчанию включают именованные схемы, такие как 'login' и 'logout'

from . import views

app_name = 'users'

urlpatterns = [
	#Включить URL авторизации по умолчанию
	path('', include('django.contrib.auth.urls')), #схема страницы входа соответствует URL:
			# http://localhost:8000/user/login/. Слово users указывает, что следует обратиться
			#к users/urls.py, а login что запросы должны отправляться представлению
																	# login по умолчанию
	path('register', views.register, name='register'),
]