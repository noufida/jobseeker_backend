from django.contrib import admin
from .models import Account,Resume,Profile,SkillSet,Experience,Qualification

# Register your models here.
admin.site.register(Account)
admin.site.register(Resume)
admin.site.register(Profile)
admin.site.register(SkillSet)
admin.site.register(Experience)
admin.site.register(Qualification)