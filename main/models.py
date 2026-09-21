import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, default="")
    description = models.TextField()
    # category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField(null=True, blank=True)
    ended_at = models.DateField(null=True, blank=True)
    is_ongoing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True) # path static atau URL
    project_url = models.URLField(blank=True, null=True) # Link ke prototype Figma
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

