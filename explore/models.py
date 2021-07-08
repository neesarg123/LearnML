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
	
	# other interactions:
	# helpful, visual, concise
	helpfuls = models.ManyToManyField(User, default=None, blank=True, related_name='helpfuls')
	visual_likes = models.ManyToManyField(User, default=None, blank=True, related_name='visual_likes')
	concise_likes = models.ManyToManyField(User, default=None, blank=True, related_name='concise_likes')

	@property
	def num_likes(self):
		return self.likes.all().count()

	@property
	def num_helpfuls(self):
		return self.helpfuls.all().count()

	@property
	def num_visual_likes(self):
		return self.visual_likes.all().count()

	@property
	def num_concise_likes(self):
		return self.concise_likes.all().count()

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


class Helpful(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	HELPFUL_CHOICES = [
		('Helpful', 'Helpful'),
		('Unhelpful', 'Unhelpful'),
	]

	value = models.CharField(choices=HELPFUL_CHOICES, max_length=10)

	def __str__(self):
		return str(self.post)


class Visual(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	VISUAL_CHOICES = [
		('Visual', 'Visual'),
		('Bland', 'Bland'),
	]

	value = models.CharField(choices=VISUAL_CHOICES, max_length=10)

	def __str__(self):
		return str(self.post)


class Concise(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	CONCISE_CHOICES = [
		('Concise', 'Concise'),
		('Wordy', 'Wordy'),
	]

	value = models.CharField(choices=CONCISE_CHOICES, max_length=10)

	def __str__(self):
		return str(self.post)