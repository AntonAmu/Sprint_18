from django import forms
from .models import Order, Book, CustomUser
from authentication.models import CustomUser 
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        # book = models.ForeignKey(Book, on_delete=models.CASCADE)
        # created_at = models.DateTimeField(auto_now_add=True, editable=False)
        # end_at = models.DateTimeField(null=True)
        fields = ['user', 'book', 'plated_end_at']
        widgets = {'plated_end_at': DateInput()}
        #user =  forms.ModelChoiceField(CustomUser.objects.all(), empty_label = None, to_field_name = 'user')
        # widgets = {
        #     'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs = {'class': 'form-control'})
        # }

    def clean(self):
        # user =  self.cleaned_data['user']
        # book = self.cleaned_data['book']
        # created_at = self.cleaned_data['created_at']
        # end_at = self.cleaned_data['end_at']
        # if Order.objects.filter(first_name = first_name).filter(last_name = last_name).count():
        #     raise ValidationError("Such user has been already created")
        # if Order.objects.filter(email = email).count():
        #     raise ValidationError("User with such email has been already created")
        return self.cleaned_data

class UpdateOrderForm(OrderForm):
    
    def clean(self):
        user =  self.cleaned_data['user']
        book = self.cleaned_data['book']
        plated_end_at = self.cleaned_data['plated_end_at']
        return self.cleaned_data