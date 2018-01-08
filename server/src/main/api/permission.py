from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    message = 'You must be admin to make a post request'
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_staff