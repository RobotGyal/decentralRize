# Generated by Django 3.0.7 on 2020-07-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_business_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.FileField(blank=True, upload_to='business_img'),
        ),
    ]
