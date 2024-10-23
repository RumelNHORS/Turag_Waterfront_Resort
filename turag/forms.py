from django import forms
from .models import Booking, Contact


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'room', 'adult', 'children', 'checkin', 'checkout', 'have_to_pay']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'adult': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'children': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'checkin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'checkout': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'have_to_pay': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount to Pay'}),
        }
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']   