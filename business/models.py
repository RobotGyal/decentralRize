from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.FileField(upload_to='business_img', blank=True)



    def __str__(self):
        return self.name
