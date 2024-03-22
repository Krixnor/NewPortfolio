from django.db import models

# Create your models here.

class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} sent by {self.email}"

class Education(models.Model):
    education = models.CharField(max_length =100)
    description = models.CharField(max_length =300)

    pass


class Skills(models.Model):
    
    pass


class Porfolio(models.Model):
    pass
