from django.db import models
from django.utils.html import mark_safe


class Business(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.FileField(upload_to='business_img', blank=True)



    def __str__(self):
        return self.name

    def image_tag(self):
            return mark_safe(f'<img src="/business_img/{self.image}" width="150" height="150" />')

    image_tag.short_description = 'Image'