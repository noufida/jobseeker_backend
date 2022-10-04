from django.contrib import admin
from .models import Category,Employer,Job,Skill,JobApplication,Location
# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class JobAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

admin.site.register(Category)
admin.site.register(Employer)
admin.site.register(Job,JobAdmin)
admin.site.register(Skill)
admin.site.register(JobApplication)
admin.site.register(Location)
