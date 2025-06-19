from django import forms
from .models import Planta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlantaForm(forms.ModelForm) :
    class Meta:
        model = Planta
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']