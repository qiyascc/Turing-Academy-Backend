from django.db import models

class Partner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='partner_images/')

    def __str__(self):
        return self.title