from django.db import models

# Create your models here.

# user schema
class UserModel(models.Model):
    username = models.CharField(max_length=30) # string
    email = models.CharField(max_length=30) # string
    password = models.CharField(max_length=30) # string
    
    def __str__(self):
        return self.username