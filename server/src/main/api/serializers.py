from rest_framework import serializers

from ..models import (Car, Workshop, Project, Event, Timeline, Member, Organiser)


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_id',
            'car_password',
            'car_type',
        ]

class WorkshopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = [
            'name',
            'venue',
            'logo_url',
            'description',
            'reg_start_date',
            'reg_end_date',
            'start_date',
            'end_date',
            'reg_status',
            'price',
            'team_limit',
            'status']


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'date',
            'status',
            'img',
            'logo',
            'offical_link'
            ]


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = [
            'name',
            'tech',
            'details',
            'img',
            'workshop'
        ]


class TimelineModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Timeline
        fields = [
            'date',
            'venue',
            'event',
            'achievement'
        ]


class MemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Member
        fields = [
            'name',
            'student_no',
            'year',
            'branch',
            'img',
            'category',
            'department',
            'fb_id'
        ]


class OrganiserModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Organiser
        fields = [
            'workshop',
            'member_id',
            'contact_no'
        ]