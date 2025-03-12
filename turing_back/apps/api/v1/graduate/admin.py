from django.contrib import admin
from .models import Graduate

@admin.register(Graduate)
class GraduateAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'position', 'youtube_link')
    search_fields = ('name', 'specialty', 'position')