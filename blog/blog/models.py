from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
		'auth.User', # not understood this part
		on_delete=models.CASCADE
		# many -to - one relation ship
		# a user can author many blog posts
	)
	body = models.TextField()
	
	def __str__(self):
		return self.title