from django.db import models


class phone(models.Model):
	ngo = models.CharField(max_length = 100)
	phone_no=models.IntegerField()
	no_likes = models.IntegerField(default =0)
	def __str__(self):
		return self.ngo+":"+str(self.phone_no)

class Quote(models.Model):
	text=models.CharField(max_length = 300)
	author=models.CharField(max_length = 100)
	def __str__(self):
		return self.text

# Create your models here.
