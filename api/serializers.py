from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    