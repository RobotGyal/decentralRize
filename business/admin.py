from django.contrib import admin

from .models import Business

admin.site.register(Business)

fields = ['image_tag']
readonly_fields = ['image_tag']