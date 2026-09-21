from rest_framework import permissions
from .policies import ProfilePolicy


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner.
        return ProfilePolicy.can_edit_profile(request.user, obj)


class IsProfileOwner(permissions.BasePermission):
    """
    Permission to only allow owners of a profile to access it.
    """

    def has_object_permission(self, request, view, obj):
        # obj is expected to be a Profile instance
        return ProfilePolicy.can_edit_profile(request.user, obj)