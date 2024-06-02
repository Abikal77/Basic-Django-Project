from django.db import models

class Blog(models.Model):
    title= models. CharField(max_length=255)
    description= models.CharField(max_length=255)
    pub_date= models.DateTimeField()
    image= models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title

    def better_pub_date(self):
        return self.pub_date.strftime("%B %d, %Y")