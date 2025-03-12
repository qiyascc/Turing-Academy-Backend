from django.db import models

class Speciality(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    apply_url = models.URLField()
    apply_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Syllabus(models.Model):
    speciality = models.ForeignKey(Speciality, related_name="syllabus", on_delete=models.CASCADE)
    file = models.FileField(upload_to='syllabus_files/', null=True, blank=True)

    def __str__(self):
        return f"Syllabus for {self.speciality.title}"

class Content(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name="contents", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.syllabus.speciality.title}"

class Instructor(models.Model):
    speciality = models.ForeignKey(Speciality, related_name="instructors", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='instructor_images/')
    linkedin_url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.speciality.title}"

class SpecialityFAQ(models.Model):
    speciality = models.ForeignKey(Speciality, related_name="faqs", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"FAQ: {self.title} - {self.speciality.title}"