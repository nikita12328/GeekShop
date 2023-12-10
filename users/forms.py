from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    # переопределяем поля для указания стилей
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Пароль'}))

    # Связываем с моделью, чтобы django понимал, с какой моделью будем работать
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    # переопределяем поля для указания стилей
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Фамилия'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    # переопределяем поля для указания стилей
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']
