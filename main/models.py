import uuid
from django.contrib.auth.models import User
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
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField(null=True, blank=True)
    ended_at = models.DateField(null=True, blank=True)
    is_ongoing = models.BooleanField(default=False)
    starred_by = models.ManyToManyField(
        User,
        related_name="starred_experiences",
        blank=True
)

    def __str__(self):
        return self.title


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(
        User,
        related_name="starred_projects",
        blank=True
    )

