from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    apply_url = models.URLField()
    apply_status = models.BooleanField(default=True)
    slots = models.PositiveIntegerField()
    last_registration_date = models.DateField()
    event_date = models.DateField()
    is_paid = models.BooleanField(default=False)  # Ücretli mi?
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Ücret

    def save(self, *args, **kwargs):
        if not self.is_paid:
            self.price = None  # Ücretsizse fiyatı null yap
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Guest(models.Model):
    event = models.ForeignKey(Event, related_name="guests", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    image = models.ImageField(upload_to='guest_images/')

    def __str__(self):
        return f"{self.name} ({self.event.title})"

class Gallery(models.Model):
    event = models.ForeignKey(Event, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_gallery/')

    def __str__(self):
        return f"Gallery Image for {self.event.title}"
