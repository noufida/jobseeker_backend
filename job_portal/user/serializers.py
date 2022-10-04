from dataclasses import fields
from .models import Account,Resume,Profile,Qualification,Experience,SkillSet
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','is_superuser','last_login','first_name','last_name','mobile','email','password','is_active','is_staff','is_superuser']

        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['is_active'] 


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__' 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__' 

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        fields='__all__' 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__' 

class SkillSetSerializer(serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    class Meta:
        model=SkillSet
        fields='__all__' 