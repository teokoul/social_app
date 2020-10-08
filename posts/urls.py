from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
	RepostView,
	PostCreateView,
	PostDetailView,
	PostListView,
	PostUpdateView,
	PostDeleteView
	)

app_name = "posts"

urlpatterns = [
	path('', RedirectView.as_view(url="/")),
    path('search/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/repost/', RepostView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]