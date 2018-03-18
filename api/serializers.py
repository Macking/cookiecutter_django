from rest_framework import serializers
from api.models import Api


class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def echo(self, validated_data):
        return Api.objects.create(**validated_data)
