from dataclasses import fields
from .models import Employer,Job,Skill,Category,JobApplication,Favourite,Location
from rest_framework import serializers
from user.serializers import AccountSerializer

class EmployerSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    class Meta:
        model = Employer
        fields = '__all__'
        

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    company = EmployerSerializer(many=False)
    category = CategorySerializer(many=False)
    location = LocationSerializer(many=False)
    class Meta:
        model = Job
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    job = JobSerializer(many=False)
    class Meta:
        model = JobApplication
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    job = JobSerializer(many=False)
    class Meta:
        model = Favourite
        fields = '__all__'