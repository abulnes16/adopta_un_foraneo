from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password': 'Contraseña'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password',
                }
            )
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        choices = (('1', 'Femenino'), ('2', 'Masculino'), ('3', 'Otros'))
        model = Profile
        fields = ['role', 'name', 'last_name', 'birth_date', 'id_number', 'gender', 'phone_number']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control', 'id': 'role'}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'id': 'name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name'
            }),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'id': 'birth_date'}, years=range(1950, 2020)),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_number'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender'}, choices=choices),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number'})
        }
