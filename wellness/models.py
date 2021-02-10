from django.db import models
from django.utils.html import mark_safe


class Wellness(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(default='Description')
    source = models.CharField(max_length=200)
    image = models.FileField(upload_to='wellness_img', blank=True)


    def __str__(self):
        return self.name

    def image_tag(self):
            return mark_safe('<img src="%s" width="150" height="150" />' % self.image.url)

    image_tag.short_description = 'Image'




