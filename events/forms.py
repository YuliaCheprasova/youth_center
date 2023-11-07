from django import forms
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
            'organizers': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

