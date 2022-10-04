
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


# for viewset router setup
router = DefaultRouter()
router.register('location',views.LocationViewSet,basename='location'),
router.register('category',views.CategoryViewSet,basename='category')
urlpatterns = [
    path('regs/', views.regs,name='regs'),
    path('emp_account/', views.emp_account,name='emp_account'),
    path('emp/', views.emp,name='emp'),
    path('emp_ad/<str:id>/', views.emp_ad,name='emp_ad'),
    path('allow/<str:id>/', views.approve,name='approve'),
    path('emp_edit/', views.edit_emp,name='edit_emp'),
    path('job_categories/', views.categories,name='categories'),

    path('register/', views.register_employer,name='register_employer'),
    path('post_job/', views.post_job,name='post_job'),
    path('<str:id>/jobs/', views.get_jobs,name='get_jobs'),
    path('post_job/<str:id>/', views.job_detail,name='job_detail'),

    path('<str:id>/add_skill/', views.add_skill,name='add_skill'),
    path('<str:id>/get_skills/', views.get_skills,name='get_skills'),
    path('<str:id>/delete_skill/<str:skill_id>/', views.delete_skill,name='delete_skill'),

    path('jobs/', views.jobs,name='jobs'),
    path('jobs/<str:id>/', views.job_des,name='job_des'),
    path('jobs/<str:id>/jd/', views.jd,name='jd'),
    path('jobs/<str:id>/update_jd/', views.update_jd,name='update_jd'),
    path('jobs/<str:id>/edit/', views.job_edit,name='job_edit'),
    path('jobs/<str:id>/status/', views.status_change,name='status_change'),


    path('jobs/<str:id>/applicants/', views.applicants,name='applicants'),
    path('jobs/<str:id>/skills/', views.skill_for_job,name='skill_for_job'),

    path('applicants/<str:id>/', views.app_details,name='app_details'),
    path('app_exp/<str:id>/', views.app_exp,name='app_exp'),
    path('app_qual/<str:id>/', views.app_qual,name='app_qual'),
    path('app_skills/<str:id>/', views.app_skills,name='app_skills'),

    path('job_/', views.JobSearchAPIView.as_view()),
    path('filter/<str:filter>/<str:location>/', views.filter_jobs,name='filter_jobs'),
    path('<str:id>/myjobs/', views.my_jobs,name='myjobs'),
    path('save/', views.saved,name='saved'),

    path('pie/', views.pie,name='pie'),
    path('bar/', views.bar,name='bar'),
] +router.urls