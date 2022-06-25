from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    caption_name = forms.CharField()
    author_name = forms.CharField()
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['caption_name', 'profile_image', 'author_name']