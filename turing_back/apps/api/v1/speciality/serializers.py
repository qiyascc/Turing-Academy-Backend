from rest_framework import serializers
from .models import Speciality, Syllabus, Content, Instructor, SpecialityFAQ

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'description']

class SyllabusSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Syllabus
        fields = ['file', 'contents']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'position', 'image', 'linkedin_url']

class SpecialityFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityFAQ
        fields = ['title', 'description']

class SpecialitySerializer(serializers.ModelSerializer):
    syllabus = SyllabusSerializer(many=True, read_only=True)
    instructors = InstructorSerializer(many=True, read_only=True)
    faqs = SpecialityFAQSerializer(many=True, read_only=True)

    class Meta:
        model = Speciality
        fields = [
            'id', 'title', 'description', 'apply_url', 'apply_status',
            'syllabus', 'instructors', 'faqs'
        ]