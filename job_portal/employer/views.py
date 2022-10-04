
from ast import Return
from logging import exception
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from user.models import Account, Experience, Qualification, SkillSet
from user.serializers import AccountSerializer, ExperienceSerializer, QualificationSerializer, SkillSetSerializer

from .models import Category, Employer, Favourite,Job, JobApplication,Skill,Location
from .serializers import EmployerSerializer, FavSerializer,LocationSerializer, JobApplicationSerializer,JobSerializer,SkillSerializer,CategorySerializer
from payment.models import Order,Plan
from user.authentication import JWTAuthentication,JWTAuthenticationEmployer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def register_employer(request):
    data = request.data
    print(data,request.user,"iiii")
    try:
        
        employer = Employer.objects.create(
            user = request.user,
            company_name = data['company_name'],
            company_website = data['company_website'],
            company_email = data['company_email'],
            company_mobile = data['company_mobile'],
            company_address = data['company_address'],
            employee_count = data['employee_count'],
            description = data['description']
        )
        
        serializer = EmployerSerializer(employer, many=False)
        return Response(serializer.data)
    except:
        if Employer.objects.filter(user=request.user).exists:
            message = {'detail': 'Acoount already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@authentication_classes([JWTAuthentication])
def edit_emp(request):
    data = request.data
    try:
        employer=Employer.objects.get(user=request.user)

        employer.company_name=data['company_name']
        employer.company_website=data['company_website']
        employer.company_email=data['company_email']
        employer.company_mobile=data['company_mobile']
        employer.company_address=data['company_address']
        employer.employee_count=data['employee_count']
        employer.save()

        return Response(True)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#checking whether a user is registered a comapny
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def emp_account(request):
    try: 
        print('ppppppppp')   
        emp = Employer.objects.filter(user_id=request.user.id).exists()
        print(emp,'fffffffffff')
        return Response(emp)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#checking whether a user is registered a comapny
@api_view(['GET'])
def regs(request):
    try: 
       
        user=Account.objects.filter(is_staff=False)
        
        res=Employer.objects.filter(user__in=user)
        serializer = EmployerSerializer(res, many=True)
        return Response(serializer.data)
        
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#approving companies
@api_view(['PATCH'])
def approve(request,id):
    try: 
       
        user=Account.objects.get(id=id)
        user.is_staff=True
        user.save()
        send_mail('Registration to seekers ',
            'Hi, Your account has been activated. Please try to login.',
            'noufidap@gmail.com'
            ,[user.email]   
            ,fail_silently=False)
        return Response(True)
        
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting detils of a conpany
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def emp(request):
    try:  
        print('hellooo')
        emp = Employer.objects.get(user=request.user)
        serializer = EmployerSerializer(emp, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting detils of a conpany
@api_view(['GET'])
def emp_ad(request,id):
    try:  
        print('hellooo')
        emp = Employer.objects.get(user__id=id)
        serializer = EmployerSerializer(emp, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




#post a job by a verified employer
@api_view(['POST'])
@authentication_classes([JWTAuthenticationEmployer])
def post_job(request):
    data = request.data
    print(data)
    company=Employer.objects.filter(user=request.user).first()
    print(company,"huh")
    try:        
        job = Job.objects.create(
            company = company,
            category_id = data['category'],
            designation = data['designation'],
            vacancies = data['vacancies'],
            location_id = data['location'],
            type = data['type'],
            workmode = data['workmode'],
            experience_from = data['experience_from'],
            experience_to = data['experience_to'],
            job_description = data['job_description'],
            criteria = data['criteria'],
            payscale_from = data['payscale_from'],
            payscale_to = data['payscale_to']

        )
        print(job,"jobing")
        serializer = JobSerializer(job, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#adding skill sets for a job
@api_view(['POST'])
@authentication_classes([JWTAuthenticationEmployer])
def add_skill(request,id):
    data = request.data
    print(id,request.data,"dddd")
    try: 
        skill = Skill.objects.create(
            job_id = id,
            skill = data['skill']
        )
        serializer = SkillSerializer(skill, many=False)
        return Response(serializer.data)
    except:
       
        message = {'detail': 'Job does not exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
      

#getting categories
@api_view(['GET'])
def categories(request):
    try:     
        category = Category.objects.all()
        print(category,"ji")
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#getting skills for a job
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def get_skills(request,id):
    try:
        skill = Skill.objects.filter(job_id=id)
        print(skill,"ji")
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Job does not exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)   
     


#deleting skill for a job
@api_view(['DELETE'])
@authentication_classes([JWTAuthenticationEmployer])
def delete_skill(request,id,skill_id):
    try:     
        Skill.objects.filter(job_id=id,id=skill_id).delete()
        message={'detail':'success'}
        return Response(message,status=status.HTTP_200_OK)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting jobs of a company
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def get_jobs(request,id):
    try:    
        print("ahooy") 
        jobs = Job.objects.filter(company__user_id=id).order_by('-id')
        # j=Job.objects.get(id=14)
        # p=j.job_skill.all()
        # print(p,"jiiiiiiiiiiiiiii")
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting details of a particular job
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def job_detail(request,id):
    try:
        job = Job.objects.get(id=id)
        print(job,"ji")
        serializer = JobSerializer(job, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#getting all job
@api_view(['GET'])
def jobs(request):
    try:
        job = Job.objects.filter(status='Active')
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#getting details of a particular job
@api_view(['GET'])
def job_des(request,id):
    try:
        job = Job.objects.get(id=id)
        print(job,"ji")
        serializer = JobSerializer(job, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting jd of a job
@api_view(['GET'])
def jd(request,id):
    try:
        job = Job.objects.get(id=id)
        print(job.jd,"llllllllllllll")
        print(job,job.jd,"for jd")
        with open(f'media/{job.jd}') as file:
            lines = file.readlines()
            

        return Response(lines)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTAuthenticationEmployer])
def update_jd(request,id):
    try:
        print('kkkkkkkkk')
        print(request.data)
        job = Job.objects.get(id=id)
        print(job.jd,'kkk')
        job.jd=request.FILES['jd']
        job.save()
        return Response(True)
    except:
        message = {'detail': 'Some problem occured in updating jd'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
   
    

#editing details of a particular job
@api_view(['PATCH'])
def job_edit(request,id):
    try:
        print(request.data,'super')
        job = Job.objects.get(id=id)
        print(job)
        job.designation=request.data['designation']
        job.location_id=request.data['location']
        job.workmode=request.data['workmode']
        job.category_id=request.data['category']
        job.type=request.data['type']
        job.experience_from=request.data['experience_from']
        job.experience_to=request.data['experience_to']
        job.payscale_from=request.data['payscale_from']
        job.payscale_to=request.data['payscale_to']
        job.save()
        
        return Response(True)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#editing details of a particular job
@api_view(['PATCH'])
def status_change(request,id):
    try:
        print(request.data,'super')
        job = Job.objects.get(id=id)
        print(job)
        job.status=request.data['status']
        
        job.save()
        
        return Response(True)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



#getting skills of a particular job
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def skill_for_job(request,id):
    try:
        skills=Skill.objects.filter(job=id)
        print(skills,"ji")
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class JobSearchAPIView(generics.ListCreateAPIView):
    search_fields = ['designation','category__job_category','company__company_name','location__location']
    filter_backends = (filters.SearchFilter,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer


#getting details about authenticated company
# @api_view(['GET'])
# @authentication_classes([JWTAuthenticationEmployer])
# def emp_account(request):  
#     try:
#         print(request.user,'lllll')
        
#         employer = Employer.objects.get(user=request.user)
#         serializer = EmployerSerializer(employer,many=False)
#         return Response(serializer.data)
#     except:
#         message = {'detail': 'Some problem occured'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting candidates applied for a particular job
@api_view(['GET'])
@authentication_classes([JWTAuthenticationEmployer])
def applicants(request,id):
    try:
        print('kkkkkkkkk')
        jobapplication=JobApplication.objects.filter(job_id=id).order_by('-id')
        print(jobapplication)
        # a=[x.get(y) for x in jobapplication for y in x]
        # print(a)
        # user=Account.objects.filter(id__in=a)
        # serializer = AccountSerializer(user, many=True)
        # return Response(serializer.data)
        serializer = JobApplicationSerializer(jobapplication,many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



#getting account of applicants with a id
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def app_details(request,id):  
    print(request.data)
    try:
        print("hello")
        user=Account.objects.get(id=id)
        serializer = AccountSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def app_exp(request,id):  
    print(request.data)
    try:
        print("hello")
        exp=Experience.objects.filter(user_id=id)
        serializer = ExperienceSerializer(exp, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def app_qual(request,id):  
    print(request.data)
    try:
        print("hello")
        qual=Qualification.objects.filter(user_id=id)
        serializer = QualificationSerializer(qual, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def app_skills(request,id):  
    print(request.data)
    try:
        print("hello")
        skill=SkillSet.objects.filter(user_id=id)
        serializer = SkillSetSerializer(skill, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

#getting all job of a company
@api_view(['GET'])
def my_jobs(request,id):
    try:
        print(id,'llllll')
        job = Job.objects.filter(company_id=id)
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#filtering jobs
@api_view(['GET'])
def filter_jobs (request,filter,location):
    try:
        print(filter,type(filter),'jjjjjj')
        a=[]
        b=[]
        for x in filter[1:]:
            print('123')
            print(int(x))
            # print(int(x),'koooooo')
            if x!=' ':
                a.append(x)

        for x in location[1:]:
            print('123')
            print(int(x))
            # print(int(x),'koooooo')
            if x!=' ':
                b.append(x)
        print(a,'thissss')
        if len(a)==0 and len(b)!=0:
            job = Job.objects.filter(location__id__in=b)
            print(job,'qq')
            serializer = JobSerializer(job, many=True)
            return Response(serializer.data)

        elif len(b)==0 and len(a)!=0:
            job = Job.objects.filter(category__id__in=a)
            print(job,'qq')
            serializer = JobSerializer(job, many=True)
            return Response(serializer.data)

        elif len(a)!=0 and len(b)!=0:
            job = Job.objects.filter(category__id__in=a,location__id__in=b)
            print(job,'qq')
            serializer = JobSerializer(job, many=True)
            return Response(serializer.data)
        else:
            job = Job.objects.all()
            print(job,'qq')
            serializer = JobSerializer(job, many=True)
            return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import viewsets

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def saved(request):  
    print(request.data)
    try:
        print("hello")
        fav=Favourite.objects.filter(user=request.user)
        serializer = FavSerializer(fav, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting all job of a company
@api_view(['GET'])
def pie(request):
    try:
        li=[]
        cat=Category.objects.all()
        print(cat)
        for c in cat:
            dict={}
            count=Job.objects.filter(category=c).count()
            dict['category']=c.job_category
            dict['count']=count
            print(dict,'dict')
            li.append(dict)
        print(li,'kkkkkkkkkkkpp-o0o')
        return Response(li)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting all job of a company
@api_view(['GET'])
def bar(request):
    try:
        li=[]
        plan=Plan.objects.all()
        for x in plan:
            dict={}
            order=Order.objects.filter(order_product=x.name).count()
            dict['name']=x.name
            dict['amount']=x.amount
            dict['purchase count']=order
            li.append(dict)

        
        print(li,'kkkkkkkkkkkpp-o0o')
        return Response(li)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)