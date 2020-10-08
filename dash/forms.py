from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser
from django.core import mail
from django.contrib.auth.models import User
from django.utils import timezone


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class adminLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        field =('email', 'password', )

class updateForm(forms.Form):
    tittle = forms.TextInput()
    story = forms.Textarea()
    time_posted = timezone.now()
    post_no = forms.IntegerField()
    class Meta:
        model = CustomUser
        field = ('tittle', 'story', 'time_posted')