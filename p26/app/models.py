from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=254)
    add = models.TextField()
    photo = models.ImageField(upload_to='contacts/')


    def __str__(self):
        return self.name
    
    