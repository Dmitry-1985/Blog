from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	"""модель для написания постов"""
	title = models.CharField(max_length=200) #заголовок поста
	text = models.TextField() #содержимое поста
	date_added = models.DateTimeField(auto_now_add=True) #втоматическое установление даты
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title