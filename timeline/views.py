from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author': 'hi',
		'title': 'blog post 1',
		'content': 'content',
		'date_posted': '2020'
	},
	{
		'author': 'hi2',
		'title': 'blog post 2',
		'content': 'content2',
		'date_posted': '2021'
	}
]
def home(request):
	context = {
		'posts': posts,
		'title': 'Timeline'
	}
	return render(request, 'timeline/home.html', context)

def about(request):
	return render(request, 'timeline/about.html', {'title': 'about'})