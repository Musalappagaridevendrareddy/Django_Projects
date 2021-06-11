from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100) # here character field is used for some content 
	content = models.TextField() # but TextField can have unristricted content
	date_posted = models.DateTimeField(default=timezone.now)  # if we use auto_now_add=True in date time field it will set to exact date time posted but we cannot update the field
	# but we need to update that when it is modified
	author = models.ForeignKey(User, on_delete=models.CASCADE) # link post with the author
	# here on_delete used to say do delete the post or user is deleted then posts also deleted

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
