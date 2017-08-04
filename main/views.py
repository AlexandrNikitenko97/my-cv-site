from django.shortcuts import render, redirect
from contact.models import Contact


def home(request):
	messages = Contact.objects.all()
	return render(request, 'main/home.html', {'messages':messages})


def about_me(request):
	return render(request, 'main/about_me.html')



