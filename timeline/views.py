from django.shortcuts import render
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all(),
		'title': 'Timeline'
	}
	return render(request, 'timeline/home.html', context)

def about(request):
	return render(request, 'timeline/about.html', {'title': 'about'})