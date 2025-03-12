from rest_framework import serializers
from .models import Graduate

class GraduateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduate
        fields = ['id', 'name', 'specialty', 'position', 'youtube_link']