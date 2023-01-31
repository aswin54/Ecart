import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app.models import CustomUser


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not a Valid Phone Number')


class CustomUserForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('username', 'name','password1', 'password2', 'email','phone_no','address')

    def clean_email(self):
        mail = self.cleaned_data['email']
        mail_qs = CustomUser.objects.filter(email=mail)
        if mail_qs.exists():
            raise forms.ValidationError('This email already registered')
        return mail

    def clean_phone_no(self):
        mobile = self.cleaned_data['phone_no']
        mobile_qs = CustomUser.objects.filter(phone_no=mobile)
        if mobile_qs.exists():
            raise forms.ValidationError('This mobile number already registered')
        return mobile
