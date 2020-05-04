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
        choices = (('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otros'))
        model = Profile
        fields = ['role', 'name', 'last_name', 'birth_date', 'id_number', 'gender', 'phone_number']

        widgets = {
            'role': forms.Select(attrs={'class': 'form-control', 'id': 'role', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'id': 'name', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'required': 'true'
            }),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'id': 'birth_date', 'required': 'true'}, years=range(1950, 2020)),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_number', 'required': 'true'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender', 'required': 'true'}, choices=choices),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number', 'required': 'true'})
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        choices = (('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otros'))
        model = Profile
        fields = ['name', 'last_name','gender','phone_number', 'birth_date', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'required': 'true'
            }),
            'birth_date': forms.SelectDateWidget(
                attrs={'class': 'form-control', 'id': 'birth_date', 'required': 'true'}, years=range(1950, 2020)),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender', 'required': 'true'},
                                   choices=choices),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number', 'required': 'true'}),
            'image': forms.FileInput()
        }
