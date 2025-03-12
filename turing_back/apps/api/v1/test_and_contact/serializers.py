from rest_framework import serializers
from .models import Test, TestOption, Contact

class TestOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestOption
        fields = ['option_text']

class TestSerializer(serializers.ModelSerializer):
    options = TestOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'question', 'answer_type', 'min_words', 'options']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.answer_type == 'text':
            data.pop('options')
        elif instance.answer_type == 'options':
            data.pop('min_words')
        return data

    def get_fields(self):
        fields = super().get_fields()
        
        if hasattr(self.instance, '__iter__'):
            return fields
        
        if self.instance and self.instance.answer_type == 'text':
            fields.pop('options')
        elif self.instance and self.instance.answer_type == 'options':
            fields.pop('min_words')
        
        return fields

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'speciality_name', 'name', 'surname', 'email', 'phone', 'created_at']