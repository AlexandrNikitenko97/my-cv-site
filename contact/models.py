from django.db import models
from django.utils import timezone


class Contact(models.Model):
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	email = models.CharField(max_length=150)
	text = models.TextField()
	send_date = models.DateTimeField(default = timezone.now)
	is_read = models.BooleanField(default=False)


	def email_read(self):
		self.is_read = True
		self.save()
	

	def __str__(self):
		return self.email + " - Re: " +self.subject


