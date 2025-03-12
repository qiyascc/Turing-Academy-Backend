from django.contrib import admin
from .models import Event, Guest, Gallery

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1  

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1  

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'slots', 'apply_status', 'is_paid', 'price')
    search_fields = ('title',)
    list_filter = ('event_date', 'apply_status', 'is_paid')
    inlines = [GuestInline, GalleryInline]

admin.site.register(Event, EventAdmin)