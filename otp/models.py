from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PhoneVerification(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    uid = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    phone_number_verified = models.BooleanField(verbose_name="Phone Verified", default=False)

    def __str__(self):
        return self.phone_number