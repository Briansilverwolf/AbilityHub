from rest_framework import serializers
from .models import Skill, Experience, Education, Qualification, PrivacySettings, Profile


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'company', 'start_date', 'end_date', 'description']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'grade']


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_id']


class PrivacySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacySettings
        fields = ['id', 'show_to_everyone', 'show_to_recruiters_only', 'hide_contact_info']


class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    qualifications = QualificationSerializer(many=True, read_only=True)
    privacy_settings = PrivacySettingsSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'created_at', 'updated_at', 'skills', 'experiences', 'educations', 'qualifications', 'privacy_settings']
        read_only_fields = ['user', 'created_at', 'updated_at']

    # Optionally, we can add a method to get the user's username or other details
    # user_username = serializers.CharField(source='user.username', read_only=True)