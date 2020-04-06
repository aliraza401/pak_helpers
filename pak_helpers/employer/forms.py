from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employer


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        filds = '__all__' 
        exclude = ['user']

        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '+92 xxx xxxxxxxx'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['city'].queryset = City.objects.none()
        # self.fields['area'].queryset = Area.objects.none()


class UpdateEmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        exclude = ['user','province','area','city']
