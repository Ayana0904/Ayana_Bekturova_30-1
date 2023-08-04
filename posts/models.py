from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag)

