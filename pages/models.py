from django.db import models
from ckeditor.fields import RichTextField

class Recipe(models.Model):
    instructions = RichTextField()


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)