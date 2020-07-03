from django import forms
from django.forms import ModelForm
from sys_endereco.models import Endereco
class cadForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
