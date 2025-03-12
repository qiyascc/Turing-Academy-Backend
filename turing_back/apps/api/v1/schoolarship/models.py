from django.db import models

class Schoolarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class AboutProgram(models.Model):
    schoolarship = models.OneToOneField(Schoolarship, on_delete=models.CASCADE, related_name="about_program")
    title = models.CharField(max_length=255)
    description = models.TextField()
    slot = models.IntegerField()
    register_date = models.DateField()
    url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f"About Program for {self.schoolarship.name}"

class Step(models.Model):
    schoolarship = models.ForeignKey(Schoolarship, on_delete=models.CASCADE, related_name="steps")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Step: {self.title} - {self.schoolarship.name}"

class SchoolarshipFAQ(models.Model):
    schoolarship = models.ForeignKey(Schoolarship, on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ: {self.question} - {self.schoolarship.name}"