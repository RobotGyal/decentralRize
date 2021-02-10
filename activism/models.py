from django.db import models

class Activism(models.Model):
    action = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


    def __str__(self):
        return self.organization
