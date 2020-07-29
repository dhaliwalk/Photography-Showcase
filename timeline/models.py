from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='timeline_pics')

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})