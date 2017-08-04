from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	text = models.TextField()
	text_preview = models.TextField(max_length=200, validators=[MinLengthValidator(100)])
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)


	def publish(self):
		self.published_date = timezone.now
		self.save()


	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=30)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.text