from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from ..models import (Workshop, Project, Event, Timeline, Member, Organiser, WorkshopPlan, WorkshopFaqs, EventTeam)


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
            'theme_color'
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
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(label='Student Number', required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model= User
        fields = [
            'username',
            'email',
            'password',
            'token'
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
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect credentials please try again")

        data["token"] = "Some Random token"
        return data
