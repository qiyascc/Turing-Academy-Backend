from django.contrib import admin
from .models import Test, TestOption, Contact

class TestOptionInline(admin.TabularInline):
    model = TestOption
    extra = 1

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_type', 'get_dynamic_field')
    inlines = [TestOptionInline]

    def get_dynamic_field(self, obj):
        if obj.answer_type == 'text':
            return f"Min Words: {obj.min_words}"
        elif obj.answer_type == 'options':
            options = ", ".join([opt.option_text for opt in obj.options.all()])
            return f"Options: {options}"
        return "N/A"

    get_dynamic_field.short_description = 'Dynamic Field'
            
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'created_at')
    list_filter = ('created_at', 'speciality_name')
    search_fields = ('name', 'surname', 'email', 'phone')
    ordering = ('-created_at',)