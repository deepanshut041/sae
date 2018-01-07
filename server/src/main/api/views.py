from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Workshop, Project, Member, Timeline, Organiser, Event, WorkshopFaqs, WorkshopPlan
from .serializers import ( WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer,
                            OrganiserModelSerializer,EventModelSerializer,
                             WorkshopFaqsModelSerializer, WorkshopPlanModelSerializer)


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

    def get_plans(self, workshop_id):
        try:
            return WorkshopPlan.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get_faqs(self, workshop_id):
        try:
            return WorkshopFaqs.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get(self, request, name):
        workshop = self.get_workshop(name)
        workshop_serializer = WorkshopModelSerializer(workshop)
        workshop_id = workshop_serializer.data['id']
        projects = self.get_projects(workshop_id)
        projects_serializer = ProjectModelSerializer(projects, many=True)
        organisers = self.get_organisers(workshop_id)
        organisers_serializer = OrganiserModelSerializer(organisers, many=True)
        plans = self.get_plans(workshop_id)
        plans_serializer = WorkshopPlanModelSerializer(plans, many=True)
        faqs = self.get_faqs(workshop_id)
        faqs_serializer = WorkshopFaqsModelSerializer(faqs, many=True)

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
        workshop_response.update({"plans":plans_serializer.data})
        workshop_response.update({"faqs":faqs_serializer.data})
        
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


class EventDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404
    
    def get_timeline(self, event_id):
        try:
            return Timeline.objects.filter(event=event_id)
        except Timeline.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_event(pk)
        event_serializer = EventModelSerializer(event)
        event_id = event_serializer.data['id']
        timeline = self.get_timeline(event_id)
        timeline_serializer = TimelineModelSerializer(timeline, many=True)
        
        timeline_response = event_serializer.data
        timeline_response.update({"timeline":timeline_serializer.data})
        return Response(timeline_response)


class MemberListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberModelSerializer(members, many=True)
        return Response({"members":serializer.data})

    def post(self, request):
        serializer = MemberModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
