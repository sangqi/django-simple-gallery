from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import GalleryUser

class GalleryUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = GalleryUser
        fields = ('username', 'password1', 'password2')

class PhotoCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
