from django.core.exceptions import ValidationError
from django.db import transaction
from .selectors import ProfileSelector
from .policies import ProfilePolicy
from .models import PrivacySettings, Skill, Experience, Education, Qualification, Profile
# Placeholder imports for validation, extraction, search services
# from .utils import validate_cv_file, extract_cv_data
# from .search import index_profile


class ProfileCreationService:
    @staticmethod
    @transaction.atomic
    def create_profile_from_cv(user, cv_file, privacy_prefs=None):
        """
        Orchestrates the full UC-001 flow:
        1. Validate CV file (size, pages, format)
        2. Extract structured data (skills, experience, education, qualifications)
        3. Create PrivacySettings (if not provided)
        4. Create Profile and related objects
        5. Index profile for search (if search engine used)
        6. Return the created Profile instance.
        """
        # 1. Validate
        # validation_result = validate_cv_file(cv_file)
        # if not validation_result.is_valid:
        #     raise ValidationError(validation_result.message)
        # For now, assume validation passes

        # 2. Extract data
        # extracted = extract_cv_data(cv_file)  # returns dict with lists
        extracted = {
            'skills': [],  # placeholder
            'experiences': [],
            'educations': [],
            'qualifications': [],
        }

        # 3. Privacy settings
        if privacy_prefs is None:
            privacy_prefs = {}
        # 4. Create profile first (without privacy_settings)
        profile = Profile.objects.create(
            user=user,
        )
        # Now create privacy settings linked to the profile
        privacy_settings = PrivacySettings.objects.create(profile=profile, **privacy_prefs)

        # Create related objects (bulk create for efficiency)
        skill_objs = [Skill(profile=profile, **s) for s in extracted['skills']]
        experience_objs = [Experience(profile=profile, **e) for e in extracted['experiences']]
        education_objs = [Education(profile=profile, **ed) for ed in extracted['educations']]
        qualification_objs = [Qualification(profile=profile, **q) for q in extracted['qualifications']]

        if skill_objs:
            Skill.objects.bulk_create(skill_objs)
        if experience_objs:
            Experience.objects.bulk_create(experience_objs)
        if education_objs:
            Education.objects.bulk_create(education_objs)
        if qualification_objs:
            Qualification.objects.bulk_create(qualification_objs)

        # 5. Index for search (placeholder)
        # index_profile(profile)

        return profile

    @staticmethod
    def update_profile_privacy(user, privacy_dict):
        """Update privacy settings for user's profile."""
        profile = ProfileSelector.get_for_user(user)
        if not profile:
            raise PermissionError("Profile does not exist.")
        if not ProfilePolicy.can_privacy_update(user, profile):
            raise PermissionError("Not allowed to modify privacy settings.")
        for attr, value in privacy_dict.items():
            setattr(profile.privacy_settings, attr, value)
        profile.privacy_settings.save()
        return profile