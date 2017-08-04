from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
	text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message ...'}))
	
	class Meta:
	    model = Contact
	    fields = ('name', 'subject', 'email', 'text')
