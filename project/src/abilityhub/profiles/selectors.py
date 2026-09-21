from .models import Profile
from .querysets import ProfileQuerySet


class ProfileSelector:
    @staticmethod
    def get_by_id(profile_id):
        """Return a Profile instance by its primary key."""
        return Profile.objects.filter(id=profile_id).first()

    @staticmethod
    def get_for_user(user):
        """Return the profile belonging to the given user."""
        return Profile.objects.filter(user=user).first()

    @staticmethod
    def list_all():
        """Return all profiles (respecting privacy via visible_to in view/service)."""
        return Profile.objects.all()

    @staticmethod
    def visible_to(viewer_user):
        """Return profiles that viewer_user is allowed to see."""
        return Profile.objects.visible_to(viewer_user)

    @staticmethod
    def search_by_skill(skill_name):
        """Return profiles that have a skill matching the given name (case-insensitive)."""
        return Profile.objects.filter(skills__name__icontains=skill_name).distinct()

    @staticmethod
    def search_by_keyword(keyword):
        """
        Simple keyword search across skills, experience job titles, education institutions.
        In production, use proper search backend (Elasticsearch, PostgreSQL full-text).
        """
        from django.db.models import Q
        return Profile.objects.filter(
            Q(skills__name__icontains=keyword) |
            Q(experiences__job_title__icontains=keyword) |
            Q(experiences__company__icontains=keyword) |
            Q(educations__institution__icontains=keyword) |
            Q(educations__degree__icontains=keyword)
        ).distinct()