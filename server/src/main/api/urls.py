from django.conf.urls import re_path, include, url
from .views import CarListAPIView, WorkshopListAPIView, EventListAPIView

urlpatterns = [
    url(r'^cars/$', CarListAPIView.as_view(), name='cars'),
    url(r'^events/$', EventListAPIView.as_view(), name='events'),
    url(r'^workshops/$', WorkshopListAPIView.as_view(), name='workshops'),
]