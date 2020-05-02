from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from feed.models import service

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png',upload_to="profile_pics")

	@property
	def average_rating(self):
		user = self.user
		sum = 0
		total = 0
		for i in range(1,6):
			set = service.objects.filter(provider=user).filter(status="Completed").filter(provider_rating__isnull=False).filter(provider_rating__total=i)
			if(len(set)>0):
				total += len(set)
				sum += i*len(set)
		if(total!=0):
			return sum/total
		else:
			return 0


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)