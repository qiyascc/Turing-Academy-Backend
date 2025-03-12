from rest_framework import serializers
from .models import Community, We, Area, Advantage, ChosenBy

class WeSerializer(serializers.ModelSerializer):
    class Meta:
        model = We
        fields = [ 'title', 'description', 'sub_description','image']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['photo_name', 'photo_file']

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['title', 'description']
        

class ChosenBySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenBy
        fields = ['description', 'photo']

class CommunitySerializer(serializers.ModelSerializer):
    we = WeSerializer(many=True, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    advantages = AdvantageSerializer(many=True, read_only=True)
    chosen_by = ChosenBySerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ['id', 'name', 'we', 'areas', 'advantages', 'chosen_by']