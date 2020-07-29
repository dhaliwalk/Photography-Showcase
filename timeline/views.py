from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# def home(request):
# 	context = {
# 		'posts': Post.objects.all(),
# 		'title': 'Timeline'
# 	}
# 	return render(request, 'timeline/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'timeline/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = "/"
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'timeline/about.html', {'title': 'about'})

