from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "You do not have permission to perform this action."
    def has_permission(self, request, view):
        # Semua orang boleh membaca
        if request.method in SAFE_METHODS:
            return True

        # User harus login untuk melakukan perubahan
        if not request.user.is_authenticated:
            return False

        # Superuser boleh melakukan semua perubahan
        if request.user.is_superuser:
            return True

        # Editor hanya boleh update, tidak boleh create/delete
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )