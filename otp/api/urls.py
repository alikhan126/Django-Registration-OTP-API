from django.conf.urls import url
from .viewsets import SendOTPView, VerifyPhoneView

urlpatterns = [
    url(r'^send_otp/$', SendOTPView.as_view(), name='send_otp'),
    url(r'^verify_otp/$', VerifyPhoneView.as_view(), name='verify_otp'),
]

