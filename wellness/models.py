from django.db import models

class Wellness(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(default='Description')
    source = models.CharField(max_length=200)
    image = models.ImageField(upload_to='wellness', height_field=None, width_field=None, max_length=100, default='/Users/makeschoolloaner/dev/SPD1.5/decentralRize/static/images/alexander-w-oEpnMn1y-7A-unsplash.jpg')


    def __str__(self):
        return self.name






