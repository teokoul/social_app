import re

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from .validators import validate_content
from hashtags.signals import parsed_hashtags

from django.db.models.signals import post_save
from django.core.exceptions import ValidationError


class PostManager(models.Manager):

	def repost(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
			
		else:
			og_parent = parent_obj
			
		qs = self.get_queryset().filter(
			user=user,
			parent=og_parent
			).filter(
				timestamp__year=timezone.now().year,
				timestamp__month=timezone.now().month,
				timestamp__day=timezone.now().day,
				)

		if qs.exists():
			return None

		obj = self.model(
			parent = parent_obj,
			user = user,
			content = parent_obj.content,
			)

		obj.save()
		return obj

	def like_toggle(self, user, post_obj):
		if user in post_obj.liked.all():
			is_liked = False
			post_obj.liked.remove(user)
		else:
			is_liked = True
			post_obj.liked.add(user)
		return is_liked

class Post(models.Model):
	parent 		= models.ForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	liked 		= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
	reply		= models.BooleanField(verbose_name='Is a reply?', default=False)
	content 	= models.CharField(max_length=140, validators=[validate_content])
	update		= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	objects = PostManager()

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ['-timestamp']

	def get_parent(self):
		the_parent = self
		if self.parent:
			the_parent = self.parent
		return the_parent

	def get_children(self):
		parent = self.get_parent()
		qs = Post.objects.filter(parent=parent)
		qs_parent = Post.objects.filter(pk=parent.pk)
		return (qs | qs_parent)

def post_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		# notify a user
		user_regex = r'@(?P<username>[\w.@+-]+)'
		usernames = re.findall(user_regex, instance.content)
		# send notification to user here.

		hash_regex = r'#(?P<hashtag>[\w\d-]+)'
		hashtags = re.findall(hash_regex, instance.content)
		parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
		# send hashtag signal to user here.

post_save.connect(post_save_receiver, sender=Post)




