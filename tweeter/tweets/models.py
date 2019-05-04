import re
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_content
from django.utils import timezone
from hashtags.signals import parsed_hashtags

# Create your models here.


class TweetManager(models.Manager):
	def retweet(self,  user, parent_obj):
		if parent_obj.parent:
			og_parant = parent_obj.parent
		else:
			og_parant = parent_obj
		qs = self.get_queryset().filter(user=user, parent=og_parant).filter(
			timestamp__year=timezone.now().year,
			timestamp__month=timezone.now().month,
			timestamp__day=timezone.now().day,
		)
		if qs.exists():
			return None

		obj = self.model(
			parent=parent_obj,
			user=user,
			content=parent_obj.content,
		)
		obj.save()
		return obj


class Tweet(models.Model):
	parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.CharField(max_length=140, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	objects = TweetManager()

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	class Meta:
			ordering = ['-timestamp']


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		# notify a user
		user_regex = r'@(<username>/)'
		username = re.search(user_regex, instance.content)
		# send notification to user here.

		hash_regex = r'#(<hashtag>/)'
		hashtags = re.search(hash_regex, instance.content)
		parsed_hashtags.send(sender=instance.__class__, hashtags_list=hashtags)
	# send hashtag signal to user here.


post_save.connect(tweet_save_receiver, sender=Tweet)
