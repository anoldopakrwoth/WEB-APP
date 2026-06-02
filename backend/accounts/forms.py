from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import UserProfile


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        help_text='Use at least 8 characters and avoid common passwords.',
        widget=forms.PasswordInput(),
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(),
    )
    role = forms.ChoiceField(
        choices=[('buyer', 'Buyer'), ('farmer', 'Farmer')],
        initial='buyer',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Email already registered.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError('Passwords do not match.')
        if password:
            validate_password(password)

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'village', 'address', 'profile_picture')
