from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	POST_AUDIENCE = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('EXP', 'Expert'),
    ]

	audience = models.CharField(max_length=3, choices=POST_AUDIENCE, default='BEG',)


	def __str__(self):
		return self.title 
