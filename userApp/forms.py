from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name","surname","tcIdentity","phoneNumber"]

    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     phoneNumber_passed = cleaned_data.get("phoneNumber")
    #     len_req = "123456"
    #     if not len_req in phoneNumber_passed:
    #         raise forms.ValidationError("Lütfen telefon numaranızı kontrol edin!!")
            