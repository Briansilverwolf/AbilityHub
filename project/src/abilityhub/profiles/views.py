from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer, PrivacySettingsSerializer
from .selectors import ProfileSelector
from .services import ProfileCreationService
from .permissions import IsProfileOwner, IsOwnerOrReadOnly
from .policies import ProfilePolicy


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter by privacy and search.
        We'll use the selector for privacy and allow search by skill or keyword.
        """
        viewer_user = self.request.user
        queryset = ProfileSelector.visible_to(viewer_user)

        # Optional search parameters
        skill = self.request.query_params.get('skill')
        keyword = self.request.query_params.get('keyword')
        if skill:
            queryset = ProfileSelector.search_by_skill(skill)
        if keyword:
            queryset = ProfileSelector.search_by_keyword(keyword)

        return queryset.distinct()

    def perform_create(self, serializer):
        """
        Create a profile using the service.
        We expect the CV file to be in the request data.
        """
        cv_file = self.request.FILES.get('cv_file')
        if not cv_file:
            # If no CV file, we might still allow creating an empty profile?
            # But according to UC-001, we need a CV to create a searchable profile.
            # So we raise an error.
            raise serializers.ValidationError("CV file is required.")

        # We'll call the service to create the profile from the CV.
        # The service expects: user, cv_file, privacy_prefs (optional)
        privacy_prefs = {}
        # You can extract privacy preferences from the request data if provided
        # For now, we'll use default.

        try:
            profile = ProfileCreationService.create_profile_from_cv(
                user=self.request.user,
                cv_file=cv_file,
                privacy_prefs=privacy_prefs
            )
            # We'll set the serializer's instance to the created profile
            serializer.instance = profile
        except Exception as e:
            # Convert to a validation error or API exception
            raise serializers.ValidationError(str(e))

    def update(self, request, *args, **kwargs):
        """
        We'll allow updating privacy settings and maybe other profile data.
        For simplicity, we'll only allow updating privacy settings via this endpoint.
        For updating skills, experience, etc., we might have separate endpoints.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # We'll only update privacy settings for now.
        privacy_serializer = PrivacySettingsSerializer(instance.privacy_settings, data=request.data, partial=partial)
        privacy_serializer.is_valid(raise_exception=True)
        privacy_serializer.save()

        # If there are other fields in the request that belong to the profile, we can update them too.
        # But for now, we'll just return the updated profile.
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a profile. Only the owner can delete.
        """
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)