from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project name'}))
	creator = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project author'})) 
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}))
	technologies = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Used technologies'})) 
	screen_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Preview image URL'})) 
	source_code_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GitHub link'})) 
	project_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project link'})) 


	class Meta:
		model = Portfolio
		fields = (
			'name', 
			'creator', 
			'category', 
			'description', 
			'technologies', 
			'screen_link', 
			'source_code_link', 
			'project_link')