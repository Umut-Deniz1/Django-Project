from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name","surname","tcIdentity","phoneNumber"]

    
            