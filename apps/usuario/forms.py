# Django
from django import forms

class fLogin(forms.Form):
    username = forms.CharField(label = 'Usuario', label_suffix = '', required = True, max_length = 50, 
        error_messages = {
            'required': 'El usuario es requerido',
            'max_length': 'Ese usuario es demasiado largo',
            'blank': 'El usuario no debe estar vacío'
        }
    )
    password = forms.CharField(label = 'Contraseña', label_suffix = '', 
        widget =  forms.PasswordInput,
        error_messages = { 
            'blank': "La contraseña no debe estar vacía",
            'required': "La contraseña es requerida"
        }
    )