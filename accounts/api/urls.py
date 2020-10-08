from django.urls import path
from django.views.generic.base import RedirectView

from posts.api.views import (
	PostListAPIView,
	)

app_name = "better"

urlpatterns = [
    path(r'<str:username>/posts/', PostListAPIView.as_view(), name='list'), # /api/post/
]