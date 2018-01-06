from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Workshop, Project, Member, Timeline, Organiser, Event
from .serializers import ( WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer,
                            OrganiserModelSerializer,EventModelSerializer)


class WorkshopListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
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


class WorkshopDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    def get_workshop(self, workshop_name):
        try:
            return Workshop.objects.get(name=workshop_name)
        except Workshop.DoesNotExist:
            raise Http404
    
    def get_projects(self, workshop_id):
        try:
            return Project.objects.filter(workshop=workshop_id)
        except Project.DoesNotExist:
            raise Http404

    def get_organisers(self, workshop_id):
        try:
            return Organiser.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, name):
        workshop = self.get_workshop(name)
        workshop_serializer = WorkshopModelSerializer(workshop)
        workshop_id = workshop_serializer.data['id']
        projects = self.get_projects(workshop_id)
        projects_serializer = ProjectModelSerializer(projects, many=True)
        organisers = self.get_organisers(workshop_id)
        organisers_serializer = OrganiserModelSerializer(organisers, many=True)

        members = []
        # Fetching team member details on basis of orgnaiser
        for organiser in organisers_serializer.data:
            member_id = organiser['member_id']
            member = self.get_member(member_id)
            member_serializer = MemberModelSerializer(member)
            members.append(member_serializer.data)
        
        workshop_response = workshop_serializer.data
        workshop_response.update({"projects":projects_serializer.data})
        workshop_response.update({"organisers":members})
        return Response(workshop_response)

class EventListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
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