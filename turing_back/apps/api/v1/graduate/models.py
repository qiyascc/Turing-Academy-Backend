from django.db import models

class Graduate(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    youtube_link = models.URLField()

    def __str__(self):
        return self.name