from django import forms

from .models import Contact, Question


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
