from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

class Test(models.Model):
    ANSWER_TYPE_CHOICES = [
        ('options', 'Qapalı sual - variantlı (variantlar üçün tab dəyişdirin)'),
        ('text', 'Açıq sual - aşağıda nə qədər minimum yazı limiti var onu qeyd edin (simvol kimi)'),
    ]

    question = models.CharField(max_length=255)
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE_CHOICES)
    min_words = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question

class TestOption(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.test.question} - {self.option_text}"


class Contact(models.Model):
    speciality_name = models.JSONField(encoder=DjangoJSONEncoder)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.email}"