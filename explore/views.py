from django.shortcuts import render


posts = [
		{
		'title': 'Title', 
		'author': 'Neesarg Mistry',
		'audience': 'Beginner',
		'content': 'first post!'
		},

		{
		'title': 'Title', 
		'author': 'Vishva Mistry',
		'audience': 'Intermediate',
		'content': 'second post!'
		},

		{
		'title': 'Title', 
		'author': 'Kalu Mistry',
		'audience': 'Beginner',
		'content': 'third post!'
		},

		{
		'title': 'Title', 
		'author': 'Girish Mistry',
		'audience': 'Expert',
		'content': 'fourth post!'
		},
	]

# Create your views here.
def explore(request):
	context = {
		'posts': posts
	}
	return render(request, 'explore/explore.html', context)