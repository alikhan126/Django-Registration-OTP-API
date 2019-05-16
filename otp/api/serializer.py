from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import PhoneVerification
User = get_user_model()



class SendOTPSerializer(serializers.Serializer):
	country_code = serializers.CharField()
	phone_number = serializers.CharField()

	def validate(self, attrs):
		phone_number = '+' + attrs.get('country_code') + attrs.get('phone_number')
		if PhoneVerification.objects.filter(phone_number = phone_number).exists():
			raise serializers.ValidationError("Phone Number is already exists.")
		return attrs


class VerifyPhoneSerializer(serializers.Serializer):
    otp = serializers.CharField()