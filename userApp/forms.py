from django import forms
from .models import Users


class UserFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name","surname","tcIdentity","phoneNumber"]