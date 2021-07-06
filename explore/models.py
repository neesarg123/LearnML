from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = HTMLField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	POST_AUDIENCE = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('EXP', 'Expert'),
    ]

	audience = models.CharField(max_length=3, choices=POST_AUDIENCE, default='BEG',)
	likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')


	@property
	def num_likes(self):
		return self.likes.all().count()

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk, 'title': self.title})


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	LIKE_CHOICES = [
		('Like', 'Like'),
		('Dislike', 'Dislike'),
	]

	value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

	def __str__(self):
		return str(self.post)