from django import forms
from django.core.validators import RegexValidator
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class ContactForm(forms.Form):
    w_house = forms.CharField( label="Chiều rộng(m)", widget=forms.TextInput(attrs={'size':1, 'maxlength':3}), validators=[])
    l_house = forms.CharField(label="Chiều dài(m):", widget=forms.TextInput(attrs={'size':1, 'maxlength':3}))
    dir_house = forms.CharField(label="Hướng:", widget=forms.TextInput(attrs={'size':1, 'maxlength':3}))
    n_door = forms.CharField(label="Số cửa:", widget=forms.TextInput(attrs={'size':1, 'maxlength':3}))