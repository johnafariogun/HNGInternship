from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 200)
    track = models.CharField(max_length = 200, null=True, blank=True, default = "")
    slack_username = models.CharField(max_length = 200, null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    email = models.EmailField(max_length = 200, null=True, blank=True, default = "")

    def formatted_created_at(self):
        # this returns the formatted format of the date, but in actual storage for more precision it will still have the milliseconds measurement
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"This is {self.name}"