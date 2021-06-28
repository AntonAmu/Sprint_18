from django import forms
from .models import CustomUser 
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'middle_name', 'password', 'role', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'})
        }

    def clean(self):
        first_name =  self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(first_name = first_name).filter(last_name = last_name).count():
            raise ValidationError("Such user has been already created")
        if CustomUser.objects.filter(email = email).count():
            raise ValidationError("User with such email has been already created")
        return self.cleaned_data

class UpdateUserForm(UserForm):
    
    def clean(self):
        first_name =  self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        return self.cleaned_data