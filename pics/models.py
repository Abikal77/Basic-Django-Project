from django.db import models

class Jobs(models.Model):
    image= models.ImageField(upload_to="media/")
    description= models.CharField(max_length=100)
