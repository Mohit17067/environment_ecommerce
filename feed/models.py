from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
import star_ratings
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.shortcuts import render, get_object_or_404

all_categories = (('Pond Cleaning', 'Pond Cleaning'),
			('Tree Planting', 'Tree Planting'),
			('Maintenance of an Area', 'Maintenance of an Area'),
			('Mosquito-Killing', 'Mosquito-Killing'))
# from star_ratings import handlers

class service(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	categories = models.CharField(default="Mosquito-Killing",choices=all_categories,max_length=50)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
	date_of_creation = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=100,default="Need Help")
	provider = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="assignee")
	estimate_budget = models.IntegerField()
	expected_date_of_completion = models.DateTimeField()
	service_pre_Img = models.ImageField(default='default_incomplete.png',upload_to='before_service/')
	# complete_info = models.TextField(default="Service Completed")
	
	feedback = models.TextField(default="No Feedback")
	provider_rating = GenericRelation(Rating)
	address = models.CharField(max_length=300)
	# author = models.ForeignKey(User,on_delete=models.CASCADE)

	@property
	def complete_info(self):
		if(self.categories=="Mosquito-Killing"):
			return get_object_or_404(feedback_mosquitokilling,service=self)

		if(self.categories=="Pond Cleaning"):
			return get_object_or_404(completion_pondcleaning,service=self)

		if(self.categories=="Tree Planting"):
			return get_object_or_404(completion_treeplantation,service=self)

		return get_object_or_404(completion,service=self)

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


class feedback_mosquitokilling(models.Model):
	service = models.OneToOneField(service,on_delete=models.CASCADE)
	spray_used = models.CharField(max_length=200)
	quantity_applied = models.IntegerField()
	eliminated_standing_water = models.CharField(max_length=3,choices=(("Yes","Yes"),("No","No")))
	natural_repallant = models.CharField(default="None",max_length=200,null=True,blank=True)
	other_info = models.TextField(default="Service Completed")
	service_post_Img = models.ImageField(default='default_incomplete.png',upload_to='after_service/')


class completion_pondcleaning(models.Model):
	service = models.OneToOneField(service,on_delete=models.CASCADE)
	drainage_done = models.CharField(max_length=3,choices=(("Yes","Yes"),("No","No")))
	pond_net_used = models.CharField(max_length=3,choices=(("Yes","Yes"),("No","No")))
	automatic_skimmer = models.CharField(max_length=100,null=True,blank=True)
	vaccum = models.CharField(max_length=3,choices=(("Yes","Yes"),("No","No")))
	beneficial_bacteria = models.CharField(max_length=100,null=True,blank=True)
	algae_treatment = models.CharField(max_length=3,choices=(("Yes","Yes"),("No","No")))
	other_info = models.TextField(default="Service Completed")
	service_post_Img = models.ImageField(default='default_incomplete.png',upload_to='after_service/')

class completion_treeplantation(models.Model):
	service = models.OneToOneField(service,on_delete=models.CASCADE)
	fertilizer_used = models.CharField(max_length=100,default="Not Used")
	plant_variety = models.CharField(max_length=100)
	water_quantity = models.IntegerField()
	depth_dug = models.IntegerField()
	residential_obstruction = models.TextField(default="No Obstruction caused to any residential property")
	other_info = models.TextField(default="Service Completed")
	service_post_Img = models.ImageField(default='default_incomplete.png',upload_to='after_service/')

class completion(models.Model):
	service = models.OneToOneField(service,on_delete=models.CASCADE)
	other_info = models.TextField(default="Service Completed")
	service_post_Img = models.ImageField(default='default_incomplete.png',upload_to='after_service/')
