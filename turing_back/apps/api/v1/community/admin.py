from django.contrib import admin
from .models import Community, We, Area, Advantage, ChosenBy
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

class WeInline(admin.TabularInline):
    model = We
    extra = 1

class AreaInline(admin.TabularInline):
    model = Area
    extra = 1

class AdvantageInline(admin.TabularInline):
    model = Advantage
    extra = 1

class ChosenByInline(admin.TabularInline):
    model = ChosenBy
    extra = 1

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [WeInline, AreaInline, AdvantageInline, ChosenByInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if Community.objects.count() == 0:
            Community.objects.create(name="Community")
        if Community.objects.count() == 1:
            obj = Community.objects.first()
            return redirect(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', obj.id)
        return super().changelist_view(request, extra_context)