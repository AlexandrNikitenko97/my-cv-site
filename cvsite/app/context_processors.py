from contact.models import Contact
from blog.models import Post

def messages_count(request):
	messages = Contact.objects.filter(is_read=False)
	context = {'new_messages':messages}
	return context


def draft_posts(request):
	posts = Post.objects.filter(published_date__isnull=True)
	context = {'draft_posts':posts}
	return context