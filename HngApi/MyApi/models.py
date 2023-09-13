from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 200)
    track = models.CharField(max_length = 200)
    slack_username = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length = 200)
