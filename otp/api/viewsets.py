from twilio.rest import Client
from .serializer import SendOTPSerializer, VerifyPhoneSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from ..models import PhoneVerification
import uuid 
from rest_framework.authentication import TokenAuthentication


def otp(phone_number, uid):
    account_sid = 'ACcbadca6797869961424a529b4bb40c40'
    auth_token = 'f729aef96e5441d1e31cf7407fa0d795'
    client = Client(account_sid, auth_token)
    print(uid)

    message = client.messages \
        .create(
            body="Please use this code to Verify your Phone Number %s" % uid,
            from_='+12052088927',
            to='+'+phone_number
        )

    print(message.sid)


class SendOTPView(generics.GenericAPIView):
    allowed_methods = ('POST',)
    authentication_classes = (TokenAuthentication, )

    def get_serializer(self, *args, **kwargs):
        return SendOTPSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        country_code = serializer.validated_data['country_code']
        phone_number = serializer.validated_data['phone_number']
        phone_number = country_code + phone_number
        if phone_number.isdigit():
            uid = uuid.uuid4().hex[:6].upper()
            otp(phone_number, uid)
            phone_number = '+' + phone_number
            phone = PhoneVerification(phone_number=phone_number, user=user, uid=uid)
            phone.save()
            return Response({'data': "OTP Sent"}, status=status.HTTP_200_OK)
        else:
            error = "Special characters not allowed"
            error_response = {
                'error': error,
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)


class VerifyPhoneView(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication, )
    allowed_methods = ('POST',)

    def get_serializer(self, *args, **kwargs):
        return VerifyPhoneSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        uid = serializer.validated_data['otp']

        user = request.user
        phone = PhoneVerification.objects.get(user=user)
        if phone.uid == uid:
            phone.phone_number_verified = True
            phone.uid = ""
            phone.save()
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Congrats your phone number has been verified'}, status=status.HTTP_200_OK)