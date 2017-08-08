from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio
from .forms import PortfolioForm
from django.contrib.auth.decorators import login_required


def portfolio_list(request):
	portfolio_list = Portfolio.objects.all()
	is_active = 'all_projects'
	return render(request, 'portfolio/portfolio_list.html', {
		'portfolio_list':portfolio_list,
		'is_active':is_active
		})


def portfolio_details(request, pk):
	portfolio_item = get_object_or_404(Portfolio, pk=pk)
	return render(request, 'portfolio/portfolio_detail.html', {'portfolio_item':portfolio_item})	


def portfolio_web(request):
	portfolio_list = Portfolio.objects.filter(category='Web')
	is_active = 'web'
	return render(request, 'portfolio/portfolio_list.html', {
		'portfolio_list':portfolio_list,
		'is_active':is_active
		})


def portfolio_programs(request):
	portfolio_list = Portfolio.objects.filter(category='Program')
	is_active = 'programs'
	return render(request, 'portfolio/portfolio_list.html', {
		'portfolio_list':portfolio_list,
		'is_active':is_active
		})


def portfolio_bots(request):
	portfolio_list = Portfolio.objects.filter(category='Bots')
	is_active = 'bots'
	return render(request, 'portfolio/portfolio_list.html', {
		'portfolio_list':portfolio_list,
		'is_active':is_active
		})


def portfolio_mobile_apps(request):
	portfolio_list = Portfolio.objects.filter(category='Mobile App')
	is_active = 'mobile_apps'
	return render(request, 'portfolio/portfolio_list.html', {
		'portfolio_list':portfolio_list,
		'is_active':is_active
		})


@login_required
def portfolio_add_project(request):
	if request.method == 'POST':
		form = PortfolioForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
		return redirect('portfolio:portfolio_details', pk=project.pk)
	else:
		form = PortfolioForm()
	return render(request, 'portfolio/add_new_project.html', {'form':form})


@login_required
def portfolio_delete_project(request, pk):
	project = get_object_or_404(Portfolio, pk=pk)
	project.delete()
	return redirect('portfolio:portfolio_list')


@login_required
def portfolio_edit_project(request, pk):
	project = get_object_or_404(Portfolio, pk=pk)
	if request.method == 'POST':
		form = PortfolioForm(request.POST, instance=project)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
		return redirect('portfolio:portfolio_details', pk=project.pk)
	else:
		form = PortfolioForm(instance=project)
	return render(request, 'portfolio/edit_project.html', {'form':form})
