from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Metadata


# Create the forms

# Create user forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", 'first_name', 'last_name', 'group']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class MetadataModelForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ['title', 'reasearchline', 'contributor', 'contact', 'description', 'keyword', 'notes']

