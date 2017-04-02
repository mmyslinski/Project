from django import forms
from .models import User, Item


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        labels = {
                'username': 'Nazwa użytkownika',
                'email': 'Adres email',
                }
        help_texts = {'username': ''}


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
                'username': 'Nazwa użytkownika',\
        }
        help_texts = {'username': ''}


class ItemForm(forms.ModelForm):
    photo = forms.FileField(required=True)

    class Meta:
        model = Item
        fields = ['category', 'name', 'photo', 'description', 'owner_contact']
        labels = {
                'category': 'Kategoria',
                'name': 'Nazwa',
                'photo': 'Zdjęcie',
                'description': 'Opis',
        }
        widgets = {
                'owner_contact': forms.HiddenInput(),
        }
