from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class service(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	tags = TaggableManager()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
	date_of_creation = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=100,default="Need Help")
	provider = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="assignee")
	estimate_budget = models.IntegerField()
	expected_date_of_completion = models.DateTimeField()
	service_pre_Img = models.ImageField(default='default_incomplete.png',upload_to='before_service/')
	complete_info = models.TextField(default="Service Completed")
	service_post_Img = models.ImageField(default='default_incomplete.png',upload_to='after_service/')
	# author = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class bidders(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	budget = models.IntegerField()
	date_of_completion = models.DateTimeField()
	service = models.ForeignKey(service,on_delete=models.CASCADE)
	got_assigned = models.BooleanField(default=False)

	def __str__(self):
		return self.username.username

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.service.id})


class donators(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	fund = models.IntegerField()
	date_of_funding = models.DateTimeField(default=timezone.now)
	service = models.ForeignKey(service,on_delete=models.CASCADE)

	def __str__(self):
		return self.username.username

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.service.id})