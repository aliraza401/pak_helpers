from django import forms
from .models import Helper

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# set forms logic here



 
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class HelperForm(forms.ModelForm):

    class Meta:
        model = Helper
        fields = '__all__'
        exclude = ['profile_visible','rating','user']

        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '+92 xxx xxxxxxxx'}),
            'cnic': forms.TextInput(
                attrs={'placeholder': '12345-6890123-4'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Please enter description of max 1500 words'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']


class UpdateHelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ['profile_picture','daily_work_rate','age','description','contact_number','province','city','area','category']
