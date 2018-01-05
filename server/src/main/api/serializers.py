from rest_framework import serializers

from ..models import (Car)


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_id',
            'car_password',
            'car_type',
        ]
