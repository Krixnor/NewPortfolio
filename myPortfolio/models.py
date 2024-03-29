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
    description = models.TextField(max_length =300)

    
    def __str__(self):
        return f"{self.education} added to education"


class Skills(models.Model):
    lang = models.CharField(max_length = 10)
    img = models.ImageField(upload_to='christabel_media', blank=True, null= True)
    
    
    def __str__(self):
        return f"{self.lang} added to skill"


class Porfolio(models.Model):
    project = models.CharField(max_length =100)
    img = models.ImageField(upload_to='christabel_media', blank=True, null= True)
    

    def __str__(self):
        return f"{self.project} added to Portfolio"
    


class Service(models.Model):
    title = models.CharField(max_length =50)
    description = models.TextField(max_length =300)
    
    def __str__(self):
        return f"{self.title} added to services"
