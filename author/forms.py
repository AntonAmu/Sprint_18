from django import forms
from .models import Author
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        patronymic = self.cleaned_data['patronymic']
        if Author.objects.filter(name=name).filter(surname=surname).count():
            raise ValidationError("Such author has been already created")
        if Author.objects.filter(patronymic=patronymic).count():
            raise ValidationError("User with such patronymic has been already created")
        return self.cleaned_data


class UpdateAuthorForm(AuthorForm):

    def clean(self):
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        patronymic = self.cleaned_data['patronymic']
        return self.cleaned_data