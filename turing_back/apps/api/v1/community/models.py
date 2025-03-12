from django.db import models

WE_NAME = "Bizim fəaliyyətlərimiz"
CHOSEN_BY_NAME = "Bizi seçənlər"
COMMUNITY_NAME = "Community"

class Community(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = COMMUNITY_NAME
        verbose_name_plural = COMMUNITY_NAME

    def __str__(self):
        return self.name

class We(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="we")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    sub_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='we_images/')

    class Meta:
        verbose_name = WE_NAME
        verbose_name_plural = WE_NAME

    def __str__(self):
        return f"We: {self.description_title} - {self.community.name}"

class Area(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="areas")
    photo_name = models.CharField(max_length=255)
    photo_file = models.ImageField(upload_to='area_photos/')

    def __str__(self):
        return f"Area: {self.photo_name} - {self.community.name}"

class Advantage(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="advantages")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Advantage: {self.title} - {self.community.name}"

class ChosenBy(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="chosen_by")
    description = models.TextField()
    photo = models.ImageField(upload_to='chosen_by_photos/')

    class Meta:
        verbose_name = CHOSEN_BY_NAME
        verbose_name_plural = CHOSEN_BY_NAME

    def __str__(self):
        return f"Chosen By: {self.description[:50]} - {self.community.name}"
