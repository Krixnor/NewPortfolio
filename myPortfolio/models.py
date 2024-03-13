from django.db import models

# Create your models here.

class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
