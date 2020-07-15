from django.contrib import admin
from django.utils.html import format_html
from .models import Business

admin.site.register(Business)

@admin.register(Business) 
class BusinessAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag',]