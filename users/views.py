from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from explore.models import Post 
from django.contrib.auth.models import User
from django.views.generic import ListView


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Thanks for joining the team, {username}, go ahead and login!')
			return redirect('login')

	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	posts = Post.objects.filter(author=request.user).order_by('-date_posted')
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)  # populate the form with user info
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account was updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)  # populate the form with user info
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
		'posts': posts,
	}

	return render(request, 'users/profile.html', context)