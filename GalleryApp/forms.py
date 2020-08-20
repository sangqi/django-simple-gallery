from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import GalleryUser

class GalleryUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = GalleryUser
        fields = ('username', 'password1', 'password2')
