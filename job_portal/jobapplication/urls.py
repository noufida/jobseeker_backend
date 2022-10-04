
from django.urls import path
from . import views

urlpatterns = [
    path('jobs/<str:id>/', views.my_jobapplication,name='my_jobapplication'),
    path('jobs/<str:id>/jobapplication/<str:uid>/', views.jobapplication,name='update_app_status'),
    path('jobs/<str:id>/update_app_status/', views.update_app_status,name='update_app_status'),
    path('jobs/<str:id>/filter/<str:status>/', views.filter_application,name='filter_application'),

]   