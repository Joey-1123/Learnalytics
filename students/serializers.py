from rest_framework import serializers
from .models import Student, Mark

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'subject', 'score']

class StudentSerializer(serializers.ModelSerializer):
    # This nesting allows you to see marks inside the student JSON
    marks = MarkSerializer(many=True, read_only=True, source='mark_set') 

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_number', 'marks']