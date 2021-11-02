from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=60,
                                 widget=forms.TextInput(attrs={'class':'validate'}))
    username = forms.EmailField(max_length=60,
                                widget=forms.TextInput(attrs={'class':'validate'}))
    password1 = forms.CharField(max_length=60,
                                widget=forms.PasswordInput(attrs={'class':'validate'}))
    password2 = forms.CharField(max_length=60,
                                widget=forms.PasswordInput(attrs={'class':'validate'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.EmailField(max_length=70,
                                widget=forms.TextInput(attrs={'label':'email', 'class':'validate'}), label="email")
    class Meta:
        model = User
        fields =  ['username', 'first_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']