from rest_framework.permissions import BasePermission
from ..models import WorkshopEnrollment
from .serializers import WorkshopEnrollmentModelSerializer


class IsAdminOrReadOnly(BasePermission):
    message = 'You must be admin to make a post request'
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_staff


class IsSuperuserOrWriteOnly(BasePermission):
    message = 'You must be admin to make a post request'
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_superuser

class IsUserEnrolled(BasePermission):
    message = 'You must be Enrolled in workshop for getting access'

    def has_permission(self, request, view):
        workshop_id = request.resolver_match.kwargs.get('workshopid')
        try:
            workshop_enrollment = WorkshopEnrollment.objects.get(workshop_id=workshop_id, user_id=request.user.id, enroll_status=True)
            return True
        except WorkshopEnrollment.DoesNotExist:
            return False