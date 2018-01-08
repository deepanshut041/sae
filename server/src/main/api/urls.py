from django.conf.urls import re_path, include, url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import (WorkshopListAPIView, EventListAPIView, 
                    WorkshopDetailAPIView, EventDetailAPIView, MemberListAPIView,
                    UserRegisterAPIView, UserLoginAPIView)

urlpatterns = [
    url(r'^events/$', EventListAPIView.as_view(), name='events'),
    url(r'^workshops/$', WorkshopListAPIView.as_view(), name='workshops'),
    url(r'^workshops/detail/(?P<name>\w+)/$', WorkshopDetailAPIView.as_view(), name='workshops-details'),
    url(r'^events/detail/(?P<pk>[0-9]+)/$', EventDetailAPIView.as_view(), name='event-details'),
    url(r'^members/$', MemberListAPIView.as_view(), name='members'),
    url(r'^auth/register/$', UserRegisterAPIView.as_view(), name='user-register'),
    url(r'^auth/login/$', UserLoginAPIView.as_view(), name='user-register'),
    url(r'^auth/api-token-auth/', obtain_jwt_token),
    url(r'^auth/api-token-refresh/', refresh_jwt_token),
    url(r'^auth/api-token-verify/', verify_jwt_token),
]