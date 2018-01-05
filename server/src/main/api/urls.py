from django.conf.urls import re_path, include, url
from .views import CarListAPIView

urlpatterns = [
    url(r'^cars/$', CarListAPIView.as_view(), name='cars'),
]