from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes

# Create your views here.
import json
from rest_framework import status

import environ
import razorpay
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employer.models import Employer

from .models import Order,Plan
from .serializers import OrderSerializer,PlanSerializer
from django.conf import settings
from user.authentication import JWTAuthentication,JWTAuthenticationEmployer


@api_view(['POST'])
def start_payment(request):
    print('yaaaa')
    # request.data is coming from frontend
    amount = request.data['amount']
    name = request.data['name']

    # setup razorpay client this is the client to whome user is paying money that's you
    client =  razorpay.Client(auth=(settings.RAZORPAY_ID , settings.RAZORPAY_KEY ))

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
    # mumtiply it by 100 so it will be 50 rupees.
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})

    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next 
    # function
    order = Order.objects.create(order_product=name, 
                                 order_amount=amount, 
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def handle_payment_success(request):
    # request.data is coming from frontend
    print('kkk')
    # print(request.data)
    # res = (request.data)
    print("dsfa")
    # print(res)
    res = json.loads(request.data["response"])
    print(res)
    """res will be:
    {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
    'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    this will come from frontend which we will use to validate and confirm the payment
    """

    ord_id = ""
    raz_pay_id = "" 
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]
    print(ord_id,"loooooo")
    # get order by payment_id which we've created earlier with isPaid=False
    order = Order.objects.get(order_payment_id=ord_id)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(settings.RAZORPAY_ID , settings.RAZORPAY_KEY ))

    # checking if the transaction is valid or not by passing above data dictionary in 
    # razorpay client if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)
    print(check)
    print(order,'ordo')
    if check is None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order = Order.objects.get(order_payment_id=ord_id)
    order.isPaid = True
    order.user = request.user
    order.save()
    print('user is',request.user)
    user=Employer.objects.get(user=request.user)
    user.subscriber=True
    user.save()
    
    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)


from rest_framework import viewsets

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all().order_by('-id')
    serializer_class = PlanSerializer

import datetime
#checking validity of existing plan
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def validity(request):
    try:
        order = Order.objects.filter(user=request.user).order_by('-id').first()
        name=order.order_product
        plan = Plan.objects.filter(name=name).first()
        validity = plan.valid_days
        ordered_on=order.order_date
        now= datetime.datetime.now()
        expiry = ordered_on + datetime.timedelta(days=validity)
        print(expiry)
        if expiry.isoformat()>now.isoformat():
            return Response(True)
        else:
            return Response(False)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#getting all job of a company
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def my_plan(request):
    try:
        order = Order.objects.filter(user=request.user).order_by('-id').first()
        name=order.order_product
        plan = Plan.objects.filter(name=name).first()
        serializer = PlanSerializer(plan,many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Some problem occured'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)