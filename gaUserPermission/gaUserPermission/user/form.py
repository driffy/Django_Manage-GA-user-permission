from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import T_Profile

class SlugField(forms.CharField):
    default_validators = [validators.validate_slug]

class JoinFormUser(forms.ModelForm):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.SlugField()
    last_name = forms.SlugField()

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

class JoinFormProfile(forms.ModelForm):
    class Meta:
        model = T_Profile
        exclude = ['user']
