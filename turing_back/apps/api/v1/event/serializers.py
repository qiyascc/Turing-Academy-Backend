from rest_framework import serializers
from .models import Event, Guest, Gallery

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['name', 'work', 'linkedin_url', 'image']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']

class EventSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'apply_url', 'apply_status',
            'slots', 'last_registration_date', 'event_date', 'is_paid', 'price',
            'guests', 'gallery'
        ]
