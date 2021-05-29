from django.db import models
import os

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	course=models.CharField(max_length=30)
	email=models.EmailField()
	age=models.IntegerField()
	profile_picture=models.FileField()


	class Meta:
		db_table='student'

	def __str__(self):
	    return self.name

	def get_absolute_image(self):
	    return os.path.join('/media', self.profile_picture.url)	

	

	
	




# Create your models here.
