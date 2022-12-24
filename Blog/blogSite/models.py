from email.mime import image
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.fullName()}"


class Tag(models.Model):
    caption = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(max_length=300)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
