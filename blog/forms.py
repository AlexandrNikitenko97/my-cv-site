from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):

	class Meta:
	    model = Post
	    fields = ('title', 'text', 'text_preview')



class CommentForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)  
			if field:
				if type(field.widget) is (forms.Textarea):
					field.widget = forms.Textarea(attrs={'placeholder': 'Your comment ...', 'class': 'form-control'})
				elif type(field.widget) is (forms.TextInput):
					field.widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})



	class Meta:
	    model = Comment
	    fields = ('author', 'text')
	    


