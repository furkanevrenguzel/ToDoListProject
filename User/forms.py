from django import forms
from django.db import models


class RegisterrFormm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(
        max_length=20, widget=forms.PasswordInput(), label="Password")
    confrim = forms.CharField(
        max_length=20, label="Confirm password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar uyuşmuyor")
        context = {
            "username": username,
            "password": password
        }
        return context


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
