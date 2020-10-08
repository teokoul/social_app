from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
	PostListAPIView,
	PostCreateAPIView,
	RepostAPIView,
    LikeToggleAPIView,
    PostDetailAPIView,
	)

app_name = "better"

urlpatterns = [
	#path(r'', RedirectView.as_view(url="/")), # /post/
    path(r'', PostListAPIView.as_view(), name='list'), # /api/post/
    path(r'create/', PostCreateAPIView.as_view(), name='create'), # /post/create/
    path(r'<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path(r'<int:pk>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
    path(r'<int:pk>/repost/', RepostAPIView.as_view(), name='repost'),  # /api/post/id/post/
    #path(r'<int:pk>/', PostDetailView.as_view(), name='detail'), # /post/1/
    #path(r'<int:pk>/update/', PostUpdateView.as_view(), name='update'), # /post/1/update/
    #path(r'<int:pk>/delete/', PostDeleteView.as_view(), name='delete'), # /post/1/delete/
]
