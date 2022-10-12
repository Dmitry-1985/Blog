from django.shortcuts import render, redirect
from django.contrib.auth import login #импортируем функцию login для выполнения 
																	#входа пользователя
from django.contrib.auth.forms import UserCreationForm #импорт стандартных форм для входа

# Create your views here.

def register(request):
	"""Представление для регистрации"""
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Выполнение входа и перенаправления на домашнюю страницу
			login(request, new_user)
			return redirect('blogs:index')

	#Вывести пустую или недействительную форму
	context = {'form': form}
	return render(request, 'registration/register.html', context)