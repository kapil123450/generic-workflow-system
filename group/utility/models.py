from django.db import models

# Create your models here.
# import the standard Django Model 
# from built-in library 

# declare a new model with a name "GeeksModel" 
class Post(models.Model): 
		# fields of the model 
	name = models.CharField(max_length = 200) 
	email_address = models.CharField(max_length = 200)  
	password = models.CharField(max_length = 200) 

		# renames the instances of the model 
		# with their title name 
	def __str__(self): 
		return self.title 

