from django.contrib.auth.hashers import make_password
from django.forms import Form, ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'image', 'phone_number']
