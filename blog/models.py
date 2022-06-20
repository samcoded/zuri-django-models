from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField('created date')
    Published_date = models.DateTimeField('published date')
    
    def __str__(self):
        return self.Title
