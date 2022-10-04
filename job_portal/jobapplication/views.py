from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes,authentication_classes

from employer.models import JobApplication
from employer.serializers import JobApplicationSerializer

from user.authentication import JWTAuthentication,JWTAuthenticationEmployer


#getting status of job application
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def jobapplication(request,id,uid):
    try:
        print('kkkkkkkkk')
        application=JobApplication.objects.filter(user_id=uid,job_id=id).first()
        serializer = JobApplicationSerializer(application,many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured in updating'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#getting job aplications of a user
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def my_jobapplication(request,id):
    try:
        print('kkkkkkkkk')
        application=JobApplication.objects.filter(user_id=id).order_by('-id')
        serializer = JobApplicationSerializer(application,many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured in updating'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#changing status of job application
@api_view(['PUT'])
@authentication_classes([JWTAuthenticationEmployer])
def update_app_status(request,id):
    try:
        print('kkkkkkkkk')
        application=JobApplication.objects.get(id=id)
        application.status=request.data['status']
        application.save()
        return Response(True)
    except:
        message = {'detail': 'Some problem occured in updating'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#filtering with status of job application
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def filter_application(request,id,status):
    try:
        print('kkkkkkkkk')
        application=JobApplication.objects.filter(job_id=id,status=status)
        serializer = JobApplicationSerializer(application,many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured in filtering'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)