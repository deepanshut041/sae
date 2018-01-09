from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from ..models import (Workshop, Project, Event, Timeline, Member, Organiser, WorkshopPlan,
 WorkshopFaqs, EventTeam, ProjectMaterial, PreWorkshopMaterial, WorkshopEnrollment, UserProfile)
#  For Sending Email
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text

class WorkshopModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    class Meta: 
        model = Workshop
        fields = [
            'id',
            'name',
            'venue',
            'logo_url',
            'background_url',
            'short_description',
            'description',
            'reg_start_date',
            'reg_end_date',
            'start_date',
            'end_date',
            'reg_status',
            'status',
            'theme_color',
            'wall_status'
            ]


class EventModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'short_description',
            'description',
            'date',
            'status',
            'img',
            'logo',
            'offical_link',
            'theme_color'
            ]


class ProjectModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'tech',
            'details',
            'img',
            'workshop'
        ]


class TimelineModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Timeline
        fields = [
            'id',
            'date',
            'venue',
            'event',
            'achievement'
        ]


class MemberModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = Member
        fields = [
            'id',
            'name',
            'student_no',
            'year',
            'branch',
            'img',
            'category',
            'contact',
            'department',
            'fb_id',
            'gender'
        ]


class OrganiserModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = Organiser
        fields = [
            'id',
            'workshop',
            'member_id'
        ]

class WorkshopPlanModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = WorkshopPlan
        fields = [
            'id',
            'workshop',
            'team_limit',
            'details',
            'title',
            'price',
        ]

class WorkshopFaqsModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = WorkshopFaqs
        fields = [
            'id',
            'workshop',
            'question',
            'answer',
        ]

class EventTeamModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = EventTeam
        fields = [
            'id',
            'event',
            'member_id',
        ]


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id',
        'username',
        'email',
        'first_name',
        'last_name']

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model= User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        user_obj.is_active = False
        user_obj.set_password(password)
        user_obj.save()
        mail_subject = 'Activate your Sae-Akgec Account'
        message = render_to_string('acc_active_email.html', {
                'user': user_obj,
                'domain': 'localhost:8000',
                'uid':urlsafe_base64_encode(force_bytes(user_obj.pk)).decode(),
                'token':account_activation_token.make_token(user_obj),
            })
        to_email = email
        send_mail = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        send_mail.send()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    token = serializers.CharField(allow_blank=True, read_only=True)
    id = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(label='Student Number', required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model= User
        fields = [
            'username',
            'email',
            'password',
            'token',
            'id'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        email = data.get("email", None)
        password = data["password"]
        if not email and not username:
            raise serializers.ValidationError("username or Email is Required to login")
        
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("A Username or Email is not valid")

        if user_obj:
            if not user_obj.is_active:
                raise serializers.ValidationError("Please Verify your confirmation Email")
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect credentials please try again")
                
        payload = api_settings.JWT_PAYLOAD_HANDLER(user_obj)
        data["token"] = api_settings.JWT_ENCODE_HANDLER(payload)
        data['username'] = user_obj.get_username()
        return data

class ProjectMaterialModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = ProjectMaterial
        fields = [
            'id',
            'workshop',
            'project',
            'material_link',
            'material_name',
        ]

class PreWorkshopMaterialModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = PreWorkshopMaterial
        fields = [
            'id',
            'workshop',
            'material_detail',
            'material_link',
            'material_name',
            'material_img',
        ]

class WorkshopEnrollmentModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = WorkshopEnrollment
        fields = [
            'id',
            'user_id',
            'team_id',
            'workshop_id',
            'payment_id',
            'leader_id',
            'enroll_date',
            'is_user_local',
            'enroll_status',
        ]

class UserProfileModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user_college',
            'user_id',
            'user_contact',
            'user_address',
            'user_local',
        ]

