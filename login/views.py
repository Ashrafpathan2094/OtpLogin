from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helpers import send_otp_to_phone
from .models import *


@api_view([ 'POST'])
def send_otp(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message': 'key phone_number is required'
        })
    user = User.objects.create(
        phone_number = data.get('phone_number'),
        otp = send_otp_to_phone(data.get('phone_number'))
    )
    return Response({
        'status':200 , 'message':'Otp Sent'
    })

