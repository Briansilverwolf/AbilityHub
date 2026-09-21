from django.db import models
from django.conf import settings
from django.utils import timezone
from .managers import ProfileManager


class Skill(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True)  # e.g., beginner, intermediate, expert

    def __str__(self):
        return self.name


class Experience(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='experiences', null=True, blank=True)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Education(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='educations', null=True, blank=True)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Qualification(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='qualifications', null=True, blank=True)
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class PrivacySettings(models.Model):
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE, related_name='privacy_settings')
    show_to_everyone = models.BooleanField(default=False)
    show_to_recruiters_only = models.BooleanField(default=True)
    hide_contact_info = models.BooleanField(default=True)
    # Add more granular flags as needed

    def __str__(self):
        return f"PrivacySettings {self.id}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # privacy_settings will be created via signal or service

    objects = ProfileManager()

    def __str__(self):
        return f"Profile of {self.user.username}"

    # Entity behavior example: completeness check
    def is_complete(self):
        """Return True if essential profile data exists."""
        return (
            self.skills.exists() and
            self.experiences.exists() and
            self.educations.exists()
        )