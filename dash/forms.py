from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.core import mail


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

connection = mail.get_connection()

connection.open()
email1 = mail.EmailMessage(
        'Hello',
        'Body goes here',
        'dash@Admin.com',
        ['dash@users'],
        connection=connection,
        )
email1.send()
connection.close()


