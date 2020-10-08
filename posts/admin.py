from django.contrib import admin

from .forms import PostModelForm
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	#form = PostModelForm
	class Meta:
		model = Post
		


admin.site.register(Post, PostModelAdmin)