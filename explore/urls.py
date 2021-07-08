from django.urls import path
from . import views
from .views import like_post, helpful_post, visual_post, concise_post, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name='explore-home'),
    path('like/', like_post, name='like-post'),
    path('helpful/', helpful_post, name='helpful-post'),
    path('visual/', visual_post, name='visual-post'),
    path('concise/', concise_post, name='concise-post'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/<title>/', PostDetailView.as_view(), name='post-detail'),   
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/<title>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/<title>/delete/', PostDeleteView.as_view(), name='post-delete'),    
]