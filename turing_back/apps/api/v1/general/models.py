from django.db import models

class General(models.Model):
    main_text = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='general_videos/', blank=True, null=True)
    scholarship_activity = models.BooleanField(default=False)

    def __str__(self):
        return self.main_text