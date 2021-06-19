from django.shortcuts import render
from .models import Post


# Create your views here.
def explore(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'explore/explore.html', context)