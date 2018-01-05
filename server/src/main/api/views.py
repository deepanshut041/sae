from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Car, Workshop, Project, Member, Timeline, Organiser, Event
from .serializers import (CarModelSerializer, WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer, OrganiserModelSerializer,
                            EventModelSerializer)


class CarListAPIView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response({"results":serializer.data})

    def post(self, request):
        serializer=CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkshopListAPIView(APIView):

    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopModelSerializer(workshops, many=True)
        return Response({"workshops":serializer.data})

    def post(self, request):
        serializer = WorkshopModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventListAPIView(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventModelSerializer(events, many=True)
        return Response({"events":serializer.data})

    def post(self, request):
        serializer=EventModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)