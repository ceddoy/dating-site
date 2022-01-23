from rest_framework.permissions import BasePermission


class ForNotAuthClientPermission(BasePermission):
    """Авторизированный пользователь не может совершать регистрацию"""
    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
