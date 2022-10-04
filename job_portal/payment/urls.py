from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter


# for viewset router setup
router = DefaultRouter()
router.register('plans',PlanViewSet,basename='plans')

urlpatterns = [
    path('pay/', start_payment, name="payment"),
    path('validity/', validity, name="validity"),
    path('payment/success/', handle_payment_success, name="payment_success"),
    path('my_plan/', my_plan, name="my_plan"),
]+router.urls
