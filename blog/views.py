from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
	post_list = Post.objects.all().order_by('-published_date')
	paginator = Paginator(post_list, 6)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1) # Calls page with index 1, if page not found calls except InvalidPage
	except EmptyPage:
		posts = paginator.page(paginator.num_pages) 		# Get number of all pages 
	return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = CommentForm()
	comments = post.comment_set.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'blog/post_detail.html', {
		'form': form, 
		'post':post,
		'comments':comments,
		})


def post_drafts(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'blog/post_drafts.html', {'posts':posts})


def post_add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
		return redirect('blog:post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_add.html', {'form':form})


def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.published_date = timezone.now()
	post.save()
	return redirect('blog:post_detail', pk=pk)


def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
		return redirect('blog:post_detail', pk = post.pk)
	else:
		form = PostForm(instance = post)
	return render(request, 'blog/post_edit.html', {'form':form})


def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('blog:post_list')


def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('blog:post_detail', pk=comment.post.pk)