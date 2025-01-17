from dataclasses import fields
from pyexpat import model
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Blog, Questions


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus':True,
        'class':"form-control", 
        'id':"formGroupExampleInput", 
        'placeholder': "Enter Username",
    }))
    password  = forms.CharField(
        label= _("Password"),
        strip = False, 
        widget= forms.PasswordInput(attrs={
            'autocomplete':'current_password',
            'class':"form-control", 
            'id':"formGroupExampleInput", 
            'placeholder': "Enter Password",
        })
    )