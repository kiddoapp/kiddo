from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'name','grade' ,'school', 'email', 'userid', 'phone', 'registrationDate')