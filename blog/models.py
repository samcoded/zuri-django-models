from django.db import models

# Create your models here.
class BlogApp(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date')
    published_date = models.DateTimeField('published date')
    body = models.TextField()
    
    def __str__(self):
        return self.title
