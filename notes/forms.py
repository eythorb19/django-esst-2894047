from django import forms
from .models import Notes
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': "form-control my-5"})
        }
        labels = {
            'text': 'Write your thoughts here'
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'Django' not in title:
            raise ValidationError('We only accept notes about Django!')
        return title
    

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']