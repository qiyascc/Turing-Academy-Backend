from django.contrib import admin
from .models import Partner
from django.utils.html import mark_safe

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="auto" />')
        return "(No Image)"
        
    image_preview.short_description = 'Image Preview'