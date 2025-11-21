# api/permissions.py

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только автору объекта.
    Для остальных пользователей разрешен только безопасный метод (чтение).
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS запросы всем.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешаем запись (POST, PUT, PATCH, DELETE) только автору объекта.
        return obj.author == request.user
