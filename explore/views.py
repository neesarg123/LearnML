from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def explore(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'explore/explore.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'explore/explore.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		ordering = ['-date_posted']
		search_query = self.request.GET.get('search_post')
		audience_query = self.request.GET.get('audience_filter')
			
		object_list = self.model.objects.all().order_by('-date_posted')

		if search_query != '' and search_query is not None:
			object_list = object_list.filter(Q(title__icontains=search_query) | 
				Q(content__icontains=search_query)).distinct()

		if audience_query != '' and audience_query is not None:
			object_list = object_list.filter(audience__iexact=audience_query)
		
		return object_list


class UserPostListView(ListView):
	model = Post
	template_name = 'explore/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))	
		return self.model.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'audience', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['title', 'audience', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = '/explore'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False