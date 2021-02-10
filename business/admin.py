from django.contrib import admin
from .models import Business

class BusinessAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'image_tag','name','description','image','genre', 'address',)
    readonly_fields = ('image_tag',)

admin.site.register(Business, BusinessAdmin)
