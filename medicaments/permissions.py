from rest_framework.permissions import BasePermission
from .models import Medicament

class IsOwner(BasePermission):
    """Custom permission class to allow only pharmacy owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the pharmacy owner."""
        if isinstance(obj, Medicament):
            return obj.user == request.user
        return obj.user == request.user
