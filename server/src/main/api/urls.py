from django.conf.urls import re_path, include, url
from .views import  WorkshopListAPIView, EventListAPIView, WorkshopDetailAPIView

urlpatterns = [
    url(r'^events/$', EventListAPIView.as_view(), name='events'),
    url(r'^workshops/$', WorkshopListAPIView.as_view(), name='workshops'),
    url(r'^workshops/detail/(?P<name>\w+)$', WorkshopDetailAPIView.as_view(), name='workshops-details'),
]