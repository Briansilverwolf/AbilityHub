class ProfilePolicy:
    @staticmethod
    def can_create(user):
        """Only authenticated users can create a profile."""
        return user.is_authenticated

    @staticmethod
    def can_view(viewer_user, profile_owner_user):
        """Viewer can view profile if owner or privacy allows."""
        if viewer_user == profile_owner_user:
            return True
        # In a real app, you would check groups/permissions and privacy settings.
        # For simplicity, we allow if profile's privacy settings allow.
        # This will be checked in service/view using the profile's privacy_settings.
        return True  # placeholder

    @staticmethod
    def can_privacy_update(user, profile):
        """Only the profile owner can update privacy settings."""
        return user == profile.user

    @staticmethod
    def can_edit_profile(user, profile):
        """Only the profile owner can edit profile."""
        return user == profile.user