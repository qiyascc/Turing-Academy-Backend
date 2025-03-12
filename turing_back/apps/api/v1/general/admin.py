from django.contrib import admin
from .models import General
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'description', 'video_url', 'video_file', 'scholarship_activity')
    fields = ('main_text', 'description', 'video_url', 'video_file', 'scholarship_activity')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if General.objects.count() == 0:
            General.objects.create(main_text="General")
        if General.objects.count() == 1:
            obj = General.objects.first()
            return redirect(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', obj.id)
        return super().changelist_view(request, extra_context)