from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    """Чтение — любому аутентифицированному пользователю,
    изменение и удаление — только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
