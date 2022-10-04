from rest_framework import serializers

from .models import Order,Plan

class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class PlanSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Plan
        fields = '__all__'
   