from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .models import *


class MathForm(forms.Form):
    number1 = forms.IntegerField(label='В скольких мероприятиях в этом семестре вы участвовали в качестве главного организатора?', initial=0, widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))
    number2 = forms.IntegerField(label='В скольких мероприятиях в этом семестре вы участвовали в качестве организатора?', initial=0, widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))
    number3 = forms.IntegerField(
        label='В скольких мероприятиях в этом семестре вы участвовали в качестве волонтера?', initial=0,
        widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))
    number4 = forms.IntegerField(
        label='В скольких мероприятиях в прошлом семестре вы участвовали в качестве главного организатора?', initial=0,
        widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))
    number5 = forms.IntegerField(
        label='В скольких мероприятиях в прошлом семестре вы участвовали в качестве организатора?', initial=0,
        widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))
    number6 = forms.IntegerField(
        label='В скольких мероприятиях в прошлом семестре вы участвовали в качестве волонтера?', initial=0,
        widget=forms.NumberInput(attrs={'min': 0, 'step': 1}))


class AddEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].required = False
        self.fields['place'].required = False
        self.fields['poster'].required = False
        self.fields['docs'].required = False
        self.fields['description'].required = True
        self.fields['organizers'].required = True
        self.fields['main_organizer'].label_from_instance = lambda obj: "%s" % obj.get_full_name()


    class Meta:
        model = Event
        fields = ['title', 'slug', 'data', 'place', 'poster', 'description', 'main_organizer', 'organizers', 'docs', 'is_done']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows':10}),
            'organizers': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'data': DateTimePickerInput(),
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields=('username', 'last_name', 'first_name', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
