from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
        	form.save()
        	return redirect('contact:contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


@login_required
def message_list(request):
	message_list = Contact.objects.all().order_by('-send_date')
	paginator = Paginator(message_list, 10)
	page = request.GET.get('page')
	try:
		messages = paginator.page(page)
	except PageNotAnInteger:
		messages = paginator.page(1) # Calls page with index 1, if page not found calls except InvalidPage
	except EmptyPage:
		messages = paginator.page(paginator.num_pages)
	return render(request, 'contact/message_list.html', {'messages':messages})
  

@login_required
def message_detail(request, pk):
	message = get_object_or_404(Contact, pk=pk)
	message.email_read()
	return render(request, 'contact/message_detail.html', {'message': message})


@login_required
def message_delete(request, pk):
	message = get_object_or_404(Contact, pk=pk)
	message.delete()
	return redirect('contact:message_list')
  