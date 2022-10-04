
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,mobile,email,password=None):
        if not email:
            raise ValueError('you must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name=last_name,
            mobile=mobile,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

         
  
    def create_superuser(self,first_name,last_name,email,mobile,password):
        user=self.create_user(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateField(auto_now_add=True)
    

class Resume(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume')


    def __str__(self):
        return self.user.first_name


class Profile(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    experienced =  models.BooleanField(default=False)
    desired_job = models.CharField(max_length=30)
    desired_location = models.CharField(max_length=30)

    def __str__(self):
        return self.user.first_name
  

class Qualification(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    degree = models.CharField(max_length=30)
    college = models.CharField(max_length=50)
    joining_year = models.IntegerField()
    passout_year = models.IntegerField()

    def __str__(self):
        return self.user.first_name

class Experience(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    start = models.IntegerField()
    end = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.user.first_name


class SkillSet(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    skill = models.CharField(max_length=30)

    def __str__(self):
        return self.user.first_name

