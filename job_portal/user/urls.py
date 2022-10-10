
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('verify/', views.verify_code,name='verify'),
    path('login/', views.login_user,name='login'),
    path('get_user/', views.get_user,name='get'),
    path('edit_user/<str:id>/', views.acc_edit,name='acc_edit'),
    path('refresh/', views.refresh,name='refresh'),
    path('logout/', views.logout_user,name='logout'),
    path('forgot_password/', views.forgot_password,name='forgot_password'),
    path('resetpassword_validate/<uidb64>/<token>',views.resetpassword_validate,name='resetpassword_validate'),
    path('resume/', views.resume,name='resume'),
    path('update_resume/', views.update_resume,name='update_resume'),
    path('get_resume/<str:id>/', views.get_resume,name='get_resume'),
    path('profile/', views.profile,name='profile'),

    path('qualification/', views.qualification,name='qualification'),
    path('get_qualification/', views.get_qualification,name='get_qualification'),
    path('qualification/<str:id>/', views.delete_qualification,name='delete_qualification'),

    path('experience/', views.experience,name='experience'),
    path('get_experience/', views.get_experience,name='get_experience'),
    path('experience/<str:id>/', views.delete_experience,name='delete_experience'),
    
    path('skill_emp/', views.SkillAPIView.as_view()),
    path('skill/', views.add_skill,name='add_skill'),
    path('get_skill/', views.get_skill,name='get_skill'),
    path('skill/<str:id>/', views.delete_skill,name='delete_skill'),

    path('apply_job/<str:id>/', views.apply,name='apply'),
    path('fav_job/<str:id>/', views.fav,name='fav'),
    path('match_job/', views.match_job,name='match_job'),
    path('job_appleid_or_not/<str:id>/', views.job_appleid_or_not,name='job_appleid_or_not'),
    path('job_fav_or_not/<str:id>/', views.job_fav_or_not,name='job_fav_or_not'),
  
    path('change_password/', views.change_password,name='change_password'),
    path('staff/', views.staffs,name='staffs'),
    path('users/', views.users,name='users'),
    path('action/<str:id>/', views.action,name='action'),

]

