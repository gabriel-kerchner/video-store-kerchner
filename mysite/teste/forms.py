from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
