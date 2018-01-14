from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permission import IsAdminOrReadOnly, IsSuperuserOrWriteOnly, IsUserEnrolled
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from ..models import (Workshop, Project, Member, Timeline, Organiser, Event,
 WorkshopFaqs, WorkshopPlan, EventTeam, ProjectMaterial, PreWorkshopMaterial, WorkshopEnrollment)
from .serializers import ( WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer,OrganiserModelSerializer,EventModelSerializer,
                             WorkshopFaqsModelSerializer, WorkshopPlanModelSerializer, EventTeamModelSerializer,
                             UserRegisterSerializer,UserLoginSerializer, ProjectMaterialModelSerializer,  PreWorkshopMaterialModelSerializer,
                             WorkshopEnrollmentModelSerializer, UserModelSerializer)

from .token import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from instamojo_wrapper import Instamojo
api = Instamojo(api_key='9474b726f61d6d2cf2d420437740074e', auth_token='8db275e2aaf013cfab88614cffd02a3a', endpoint='https://www.instamojo.com/api/1.1/')

class WorkshopListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = WorkshopModelSerializer
    permission_classes = (IsAdminOrReadOnly,permissions.IsAuthenticatedOrReadOnly)
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

class LatestWorkshopListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    permission_classes = (IsAdminOrReadOnly,permissions.IsAuthenticatedOrReadOnly)
    def get_plans(self, workshop_id):
        try:
            return WorkshopPlan.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get(self, request):
        workshops = Workshop.objects.filter(reg_status=True)
        serializer = WorkshopModelSerializer(workshops, many=True)
        current_workshops = []
        for current in serializer.data:
            plans = self.get_plans(current['id'])
            plans_serializer = WorkshopPlanModelSerializer(plans, many=True)
            current.update({"plans":plans_serializer.data})
            current_workshops.append(current)
        return Response({"workshops":current_workshops})

class WorkshopDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    permission_classes = (permissions.AllowAny,)
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
    
    serializer_class = EventModelSerializer
    permission_classes = (IsAdminOrReadOnly,permissions.IsAuthenticatedOrReadOnly,)
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

class UserEnrollmentView(APIView):

    # Getting current workshop 
    def get_workshop(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404

    def get_plan(self, pk):
        try:
            return WorkshopPlan.objects.get(pk=pk)
        except WorkshopPlan.DoesNotExist:
            raise Http404
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404
    
    def post(self, request):
        data = request.data
        workshop_id = data['workshop']
        workshop = self.get_workshop(workshop_id)
        workshop_serializer = WorkshopModelSerializer(workshop)
        if not workshop_serializer['reg_status']:
            return Response({"error":"Sorry but registration are not available"}, status=status.HTTP_400_BAD_REQUEST)
        plan_id = data['plan']
        plan = self.get_plan(plan_id)
        plan_serializer = WorkshopPlanModelSerializer(plan)
        team_limit = plan_serializer.data['team_limit']
        members = data['team_members']
        if team_limit < len(members):
            return Response({"error":"Sorry but team provided exceeed team limit"}, status=status.HTTP_400_BAD_REQUEST)
        leader = members[0]
        leader_model = self.get_user(leader['email'].lower())
        leader_serializer = UserModelSerializer(leader_model)
        if not leader_serializer:
            return Response({"error":"Sorry but any of team member is not registerd"}, status=status.HTTP_400_BAD_REQUEST)

        new_members_seralizer = []
        for member in members:
            user_model = self.get_user(member['email'])
            user_serializer = UserModelSerializer(user_model)
            if not user_serializer:
                return Response({"error":"Sorry but any of team member is not registerd"}, status=status.HTTP_400_BAD_REQUEST)
            new_member = {}
            new_member['team_id'] = data['team_id']
            new_member['plan_id'] = plan_serializer.data['id']
            new_member['workshop_id'] = workshop_serializer.data['id']
            new_member['is_user_local'] = member['is_user_local']
            new_member['user_college'] = member['user_college']
            new_member['user_contact'] = member['user_contact']
            new_member['leader_id'] = leader_serializer.data['id']
            new_member['user_id'] = user_serializer.data['id']
            new_member_seralizer = WorkshopEnrollmentModelSerializer(data=new_member)
            if not new_member_seralizer.is_valid():
                print(new_member_seralizer.errors)
                return Response({"error":"Sorry any of yout team member is already registred"}, status=status.HTTP_400_BAD_REQUEST) 
            new_members_seralizer.append(new_member_seralizer)
        for serializer in new_members_seralizer:
            serializer.save()
        response = api.payment_request_create(
                amount=str(plan_serializer.data['price']),
                purpose= workshop_serializer.data['name'],
                send_email=True,
                email=leader['email'].lower(),
                buyer_name=data['team_id'],
                phone=leader['user_contact'],
                redirect_url=request.build_absolute_uri("/user/payment")
            )
        print(response)
        return Response({"link":response['payment_request']['longurl']}, status=status.HTTP_201_CREATED)



class EventDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    permission_classes = (permissions.AllowAny,)
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

    def get_team(self, event_id):
        try:
            return EventTeam.objects.filter(event=event_id)
        except EventTeam.DoesNotExist:
            raise Http404

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_event(pk)
        event_serializer = EventModelSerializer(event)
        event_id = event_serializer.data['id']
        timeline = self.get_timeline(event_id)
        timeline_serializer = TimelineModelSerializer(timeline, many=True)
        team = self.get_team(event_id)
        team_serializer = EventTeamModelSerializer(team, many=True)

        members = []
        # Fetching team member details on basis of orgnaiser
        for team_member in team_serializer.data:
            member_id = team_member['member_id']
            member = self.get_member(member_id)
            member_serializer = MemberModelSerializer(member)
            members.append(member_serializer.data)
        
        timeline_response = event_serializer.data
        timeline_response.update({"timeline":timeline_serializer.data})
        timeline_response.update({"team":members})
        return Response(timeline_response)


class MemberListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    
    serializer_class = MemberModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly)
    def get_team(self):
        try:
            return Member.objects.filter(year__gte=3)
        except Member.DoesNotExist:
            raise Http404
    def get(self, request):
        members = self.get_team()
        serializer = MemberModelSerializer(members, many=True)
        return Response({"members":serializer.data})

    def post(self, request):
        serializer = MemberModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = UserLoginSerializer
    permission_classes = (IsSuperuserOrWriteOnly,)
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response({"user":serializer.data})

class UserEmailVerificationView(View):
            
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
        return HttpResponse("Activation link is invalid!")

# User View Goes here

class ClassRoomView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_workshop(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404

    def get_enrollment(self,user_id):
        try:
            return WorkshopEnrollment.objects.filter(user_id=user_id, enroll_status=True)
        except EventTeam.DoesNotExist:
            raise Http404
    def get(self,request):
        user = User.objects.get(username=request.user.username)
        user_serializer = UserModelSerializer(user)
        user_id =  user_serializer.data['id']

        #Getting  Workshop in which user is enrolled 
        enrollments = self.get_enrollment(user_id)
        enrollments_serializer = WorkshopEnrollmentModelSerializer(enrollments, many=True)
        workshops = []
        for enrollment in enrollments_serializer.data:
            workshop = self.get_workshop(enrollment['workshop_id'])
            workshop_serializer = WorkshopModelSerializer(workshop)
            workshops.append(workshop_serializer.data)

        classroom_response ={}
        classroom_response.update({"enrollments":enrollments_serializer.data})
        classroom_response.update({"workshops":workshops}) 
        return Response(classroom_response)


class ClassCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,IsUserEnrolled,)
    def get_workshop(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404
    def get_projects(self, workshop_id):
        try:
            return Project.objects.filter(workshop=workshop_id)
        except Project.DoesNotExist:
            raise Http404
    def get_project_material(self, project):
        try:
            return ProjectMaterial.objects.filter(project=project)
        except ProjectMaterial.DoesNotExist:
            raise Http404
            
    def get_pre_workshop_material(self, workshopid):
        try:
            return PreWorkshopMaterial.objects.filter(workshop=workshopid)
        except PreWorkshopMaterial.DoesNotExist:
            raise Http404

    def get(self,request,workshopid):
        workshop = self.get_workshop(workshopid)
        workshop_serializer = WorkshopModelSerializer(workshop)
        pre_material = self.get_pre_workshop_material(workshopid)
        pre_material_serializer = PreWorkshopMaterialModelSerializer(pre_material,many=True)
        projects = self.get_projects(workshopid)
        projects_serializer = ProjectModelSerializer(projects, many=True)


        # Give projects with material emmbeded in them
        projects_response = []
        for project in projects_serializer.data:
            project_materials = self.get_project_material(project['id'])
            material_serializer = ProjectMaterialModelSerializer(project_materials, many=True)
            project['materials'] = material_serializer.data
            projects_response.append(project)

        course_response = {}
        course_response.update(workshop_serializer.data)
        course_response.update({"pre_material": pre_material_serializer.data})
        course_response.update({"projects":projects_response})
        return Response(course_response)

# Contact Email View 


class ContactUsAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        full_name = data['full_name']
        email_address = data['email']
        phone_number = data['phone_number']
        description = data['description']
        
        mail_subject = data['subject']

        if full_name and email_address and phone_number and description and mail_subject:
            mail_message = render_to_string('contact_mail.html', {
                'full_name': full_name,
                'email_address': email_address,
                'phone_number': phone_number,
                'description':description,
            })
            to_email = "saeakgec.event@gmail.com"
            send_mail = EmailMessage(
                        mail_subject, mail_message, to=[to_email]
            )
            send_mail.send()
            return Response({"status":"Email Sent"}, status=status.HTTP_201_CREATED)
        return Response({"status":"Email Not Sent"}, status=status.HTTP_400_BAD_REQUEST)   
   


