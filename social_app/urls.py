from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView
from hashtags.api.views import TagPostAPIView
from hashtags.views import HashTagView
from posts.api.views import SearchPostAPIView
from .views import home, SearchView
from posts.views import PostListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('api/search/', SearchPostAPIView.as_view(), name='search-api'),
    path('api/tags/<str:hashtag>/', TagPostAPIView.as_view(), name='tag-post-api'),
    path('tags/<str:hashtag>/', HashTagView.as_view(), name='hashtag'),
    path('posts/', include('posts.urls', namespace = 'posts')),
    path('profiles/', include('accounts.urls', namespace = 'profiles')),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls', namespace = 'profile')),
    path('api/posts/', include('posts.api.urls', namespace = 'posts-api')),
    path('api/', include('accounts.api.urls', namespace = 'accounts-api')),
]


# if settings.DEBUG:
# 	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))