from django.contrib import admin
from .models import Schoolarship, AboutProgram, Step, SchoolarshipFAQ

class AboutProgramInline(admin.StackedInline):
    model = AboutProgram
    max_num = 1
    can_delete = False

class StepInline(admin.TabularInline):
    model = Step
    extra = 1
    max_num = 3

class SchoolarshipFAQInline(admin.TabularInline):
    model = SchoolarshipFAQ
    extra = 1

@admin.register(Schoolarship)
class SchoolarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [AboutProgramInline, StepInline, SchoolarshipFAQInline]