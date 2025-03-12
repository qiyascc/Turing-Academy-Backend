from rest_framework import serializers
from .models import General

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['id', 'main_text', 'description', 'video_url', 'video_file', 'scholarship_activity']