from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.db.models import Count

# def home(request):
# 	context = {
# 		'posts': Post.objects.all(),
# 		'title': 'Timeline'
# 	}
# 	return render(request, 'timeline/home.html', context)

def leaderboard(request):
	user_posts = User.objects.annotate(total_posts = Count('post')).order_by('-total_posts')
	return render(request, 'timeline/leaderboard.html', {'user_posts': user_posts})

class PostListView(ListView):
	model = Post
	template_name = 'timeline/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10

class UserPostListView(ListView):
	model = Post
	template_name = 'timeline/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

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

