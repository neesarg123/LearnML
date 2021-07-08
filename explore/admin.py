from django.contrib import admin
from .models import Post, Like, Helpful, Visual, Concise

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Helpful)
admin.site.register(Visual)
admin.site.register(Concise)

