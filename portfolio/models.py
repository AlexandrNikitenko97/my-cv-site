from django.db import models
from django.utils import timezone


class Portfolio(models.Model):

	# CATEGORY CHOICES

	web = 'Web'
	program = 'Program'
	bots = 'Bots'
	mobile_app = 'Mobile App'
	category_choices = (
		(web, 'Web'),
		(program, 'Program'),
		(bots, 'Bots'),
		(mobile_app, 'Mobile App'),
		)

	# ---------------------------

	name = models.CharField(max_length=200)
	creator = models.CharField(max_length=100)
	category = models.CharField(max_length=10, choices=category_choices)
	description = models.TextField()
	technologies = models.CharField(max_length=300, default=None)
	screen_link = models.CharField(max_length=500)
	source_code_link = models.CharField(max_length=300, blank=True, null=True)
	project_link = models.CharField(max_length=300, blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.name + ' - ' + self.category
