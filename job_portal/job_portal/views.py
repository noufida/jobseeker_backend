

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render,redirect
from django.conf import settings

def index(request):
    return render(request,'index.html',{'url':settings.STATIC_URL})