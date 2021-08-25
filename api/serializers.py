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

# Field Lavel validation   

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Set Full')
        return value
    
    def validate_name(self, value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name is not started with R')
        return value


# object lavel validation error
    def validate(self, data):
        nm = data.get('name')
        ct= data.get('city')
        if len(nm) >= 10 and len(ct) >= 10:
            raise serializers.ValidationError('Its too large')
        return data

    