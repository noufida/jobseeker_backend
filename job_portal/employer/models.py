from django.db import models
from user.models import Account
# Create your models here.

class Employer(models.Model):    
    user = models.OneToOneField(Account,on_delete=models.CASCADE,unique=True)
    company_name = models.CharField(max_length=30)
    company_website = models.CharField(max_length=30,null=True,blank=True)
    company_email = models.EmailField(max_length=30,unique=True)
    company_mobile = models.CharField(max_length=10,unique=True)
    company_address = models.CharField(max_length=300)
    employee_count = models.IntegerField()
    description = models.TextField()
    subscriber = models.BooleanField(default=False)
   
    def __str__(self):
        return self.company_name



class Category(models.Model):
    job_category = models.CharField(max_length=30)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self) :
        return self.job_category

    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Location(models.Model):
    location = models.CharField(max_length=30)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self) :
        return self.location

    

class Job(models.Model):
    company = models.ForeignKey(Employer,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    vacancies = models.IntegerField(null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True,blank=True)
    type =models.CharField(max_length=30,default="Full time")
    workmode =models.CharField(max_length=30,default="On-site")
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    job_description = models.TextField()
    jd = models.FileField(upload_to='jd',null=True,blank=True)
    criteria = models.TextField()
    payscale_from = models.IntegerField(null=True,blank=True)
    payscale_to = models.IntegerField(null=True,blank=True)
    applicants = models.IntegerField(default=0)
    hired = models.IntegerField(default=0)
    status = models.CharField(max_length=30, default='Active', null=True,blank=True)
    created_on = models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self) :
        return self.designation
   
    
class Skill(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='job_skill')
    skill = models.CharField(max_length=30)

    def __str__(self) :
        return self.skill



class JobApplication(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default='pending')
    applied = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user.first_name

class Favourite(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    applied = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name