from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import (
	UserDetailView,
	UserFollowView
	)

app_name = "better"

urlpatterns = [
    
	# path(r'', RedirectView.as_view(url="/")), # /post/
    # path(r'search/', PostListView.as_view(), name='list'), # /post/
    # path(r'/create/', PostCreateView.as_view(), name='create'), # /post/create/
    path(r'<str:username>/', UserDetailView.as_view(), name='detail'), # /post/1/
    path(r'<str:username>/follow/', UserFollowView.as_view(), name='follow'), # /post/1/
    # path(r'<int:pk>/update/', PostUpdateView.as_view(), name='update'), # /post/1/update/
    # path(r'<int:pk>/delete/', PostDeleteView.as_view(), name='delete'), # /post/1/delete/
]
