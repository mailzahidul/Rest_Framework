from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Set Full')
        return value




class StudentCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
    
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Set Full')
        return value
    