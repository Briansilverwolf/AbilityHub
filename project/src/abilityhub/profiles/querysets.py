from django.db import models


class ProfileQuerySet(models.QuerySet):
    def with_skills(self):
        return self.filter(skills__isnull=False).distinct()

    def with_experience(self):
        return self.filter(experiences__isnull=False).distinct()

    def with_education(self):
        return self.filter(educations__isnull=False).distinct()

    def for_user(self, user):
        return self.filter(user=user)

    def visible_to(self, viewer_user):
        """
        Return profiles that the viewer_user is allowed to see based on privacy.
        Simplified: if viewer is owner, show all; else show only those with show_to_everyone=True or show_to_recruiters_only if viewer is recruiter.
        In real app, you would check groups or permissions.
        """
        from .models import PrivacySettings
        # Owner can always see own profile
        owned = self.filter(user=viewer_user)
        # Others: show profiles where privacy allows
        others = self.exclude(user=viewer_user).filter(
            models.Q(privacy_settings__show_to_everyone=True) |
            models.Q(privacy_settings__show_to_recruiters_only=True, viewer_user__groups__name='recruiters')
        )
        return (owned | others).distinct()


class SkillQuerySet(models.QuerySet):
    def top_n(self, n=10):
        return self.order_by('?')[:n]  # placeholder


# Similarly for other models if needed.