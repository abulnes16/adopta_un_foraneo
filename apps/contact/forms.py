from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'message': 'Mensaje'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control m-2', 'placeholder': 'Correo'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje',
                                             'rows': 4}),
        }
