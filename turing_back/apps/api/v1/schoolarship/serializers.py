from rest_framework import serializers
from .models import Schoolarship, AboutProgram, Step, SchoolarshipFAQ

class AboutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProgram
        fields = ['title', 'description', 'slot', 'register_date', 'url']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['title', 'description']

class SchoolarshipFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolarshipFAQ
        fields = ['question', 'answer']

class SchoolarshipSerializer(serializers.ModelSerializer):
    about_program = AboutProgramSerializer(read_only=True)
    steps = StepSerializer(many=True, read_only=True)
    faqs = SchoolarshipFAQSerializer(many=True, read_only=True)

    class Meta:
        model = Schoolarship
        fields = ['id', 'name', 'description', 'about_program', 'steps', 'faqs']