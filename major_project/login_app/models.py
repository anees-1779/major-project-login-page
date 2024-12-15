from django.db import models
 
# Create your models here.
class user_auth(models.Model):
  user_id= models.IntegerField()
  password = models.CharField( max_length=128)
  

