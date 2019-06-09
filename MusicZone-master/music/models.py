from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Permission

class Album(models.Model):
	user = models.ManyToManyField(User)
	title=models.CharField(max_length=300)
	artist=models.CharField(max_length=200)
	genre=models.CharField(max_length=100)
	logo=models.FileField()
	fav = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('album-detail',args=[str(self.id)])

	def __str__(self):
		return self.title + ' (' +self.artist + ')'

class Song(models.Model):
	user = models.ManyToManyField(User)
	title=models.CharField(max_length=300)
	album=models.ForeignKey('Album',on_delete=models.CASCADE)
	fav=models.BooleanField(default=False)
	audio=models.FileField(default='')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('song-detail',args=[str(self.id)])

