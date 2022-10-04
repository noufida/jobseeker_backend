from dataclasses import fields
from .models import Application,Fav
from rest_framework import serializers
from user.serializers import AccountSerializer
from employer.serializers import JobSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    job = JobSerializer(many=False)
    class Meta:
        model = Application
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    job = JobSerializer(many=False)
    class Meta:
        model = Fav
        fields = '__all__'