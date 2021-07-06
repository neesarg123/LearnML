from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	fb_link = models.URLField(blank=True, max_length=100, default='#')
	linkedin_link = models.URLField(blank=True, max_length=100, default='#')
	twitter_link = models.URLField(blank=True, max_length=100, default='#')
	insta_link = models.URLField(blank=True, max_length=100, default='#')


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 170 or img.width > 170:
			output_size = (170, 170)
			img.thumbnail(output_size)
			img.save(self.image.path)
