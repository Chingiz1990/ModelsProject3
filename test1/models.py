from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.text