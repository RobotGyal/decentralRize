from django.db import models

class Wellness(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(default='Description')
    source = models.CharField(max_length=200)
    image = models.FileField(upload_to='wellness_img', blank=True)


    def __str__(self):
        return self.name






