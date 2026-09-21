from django.db import models
from .querysets import ProfileQuerySet


class ProfileManager(models.Manager):
    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db)

    def with_skills(self):
        """Return profiles that have at least one skill."""
        return self.get_queryset().with_skills()

    def for_user(self, user):
        """Return the profile for a given user."""
        return self.get_queryset().for_user(user).first()