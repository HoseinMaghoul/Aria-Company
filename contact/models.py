from django.db import models
from datetime import datetime
# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    number = models.IntegerField(blank=True, null=True)
    text = models.TextField()



    def __str__(self):
        return f'{self.name}-{self.text[:20]}'


