from django import forms
from apps.polla.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'username',
            'password',
        ]

        labels = {
            'username' : 'Username',
            'password' : 'Contrasena',
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'type':'password','class':'form-control'}),
        }
