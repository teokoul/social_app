from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import ( 
	DetailView, 
	ListView, 
	CreateView, 
	UpdateView, 
	DeleteView 
)

from .forms import PostModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Post

class RepostView(View):

	def get(self, request, pk, *args, **kwargs):
		post = get_object_or_404(Post, pk=pk)
		if request.user.is_authenticated:
			new_post = Post.objects.repost(request.user, post)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(posts.get_absolute_url())

class PostCreateView(FormUserNeededMixin, CreateView):
	form_class = PostModelForm
	template_name = 'posts/create_view.html'
	#success_url = reverse_lazy('posts:detail')
	login_url = '/admin/'

class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Post.objects.all()
	form_class = PostModelForm
	template_name = 'posts/update_view.html'
	success_url = '/posts/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'posts/delete_view.html'
	success_url = reverse_lazy('posts:list') 

class PostDetailView(DetailView):
	queryset = Post.objects.all()

class PostListView(LoginRequiredMixin, ListView):
	# Searching
	def get_queryset(self, *args, **kwargs):
		qs = Post.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs


	def get_context_data(self, *args, **kwargs):
		context = super(PostListView,self).get_context_data(*args, **kwargs)
		context['create_form'] = PostModelForm()
		context['create_url'] = reverse_lazy("posts:create")
		return context

