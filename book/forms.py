from django import forms
from .models import Book
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count']
        # widgets = {
        #     'name': forms.CharField(attrs={'class': 'form-control'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'count': forms.IntegerField(attrs={'class': 'form-control'})
        #     # 'authors': forms.TextInput(attrs={'class': 'form-control'})
        # }

    def clean(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        count = self.cleaned_data['count']
        if Book.objects.filter(name=name).filter(description=description).count():
            raise ValidationError("Such author has been already created")
        if Book.objects.filter(count=count).count():
            raise ValidationError("User with such patronymic has been already created")
        return self.cleaned_data


class UpdateBookForm(BookForm):

    def clean(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        count = self.cleaned_data['count']
        return self.cleaned_data