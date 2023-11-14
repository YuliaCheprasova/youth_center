from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .models import *

class AddEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].required = False
        self.fields['place'].required = False
        self.fields['poster'].required = False
        self.fields['docs'].required = False
        self.fields['description'].required = True
        self.fields['organizers'].required = True

    class Meta:
        model = Event
        fields = ['title', 'slug', 'data', 'place', 'poster', 'description', 'main_organizer', 'organizers', 'docs', 'is_done']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows':10}),
            'organizers': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'data': DateTimePickerInput()
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')
