from django.contrib import admin
from .models import Speciality, Syllabus, Content, Instructor, SpecialityFAQ

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

class SyllabusInline(admin.TabularInline):
    model = Syllabus
    extra = 1

class InstructorInline(admin.TabularInline):
    model = Instructor
    extra = 1

class SpecialityFAQInline(admin.TabularInline):
    model = SpecialityFAQ
    extra = 1

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('title', 'apply_status')
    search_fields = ('title',)
    inlines = [InstructorInline, SpecialityFAQInline]

# @admin.register(Syllabus)
# class SyllabusAdmin(admin.ModelAdmin):
#     inlines = [ContentInline]

# @admin.register(Instructor)
# class InstructorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'position', 'speciality')

# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ('title', 'speciality')