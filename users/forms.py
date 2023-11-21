from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ValidationError

from .models import User, Role, Office


class UserCreationForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #   super(UserCreationForm, self).__init__(*args, **kwargs)
      # try:
      #   role_obj = args[0].pop('role', '')
      # except Exception as e:
      #   role_obj = {id: }
      #   role_obj.id = 4
      # print(args)
    role = forms.ModelChoiceField(label='Роль', queryset=Role.objects.all(), required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    office = forms.ModelChoiceField(label='Офис', queryset=Office.objects.all(), required=False)
    date_of_birth = forms.DateField(label='Дата рождения', required=False)
    is_active = forms.BooleanField(label='Активный', required=False)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def clean_role(self):
        role = self.cleaned_data.get("role")
        return role

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        return last_name

    def clean_office(self):
        office = self.cleaned_data.get("office")
        return office

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")
        return date_of_birth

    def clean_is_active(self):
        is_active = self.cleaned_data.get("is_active")
        return is_active

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if self.cleaned_data.get("role", False):
            user.role = self.cleaned_data["role"]
        if self.cleaned_data.get("first_name", False):
            user.first_name = self.cleaned_data["first_name"]
        if self.cleaned_data.get("last_name", False):
            user.last_name = self.cleaned_data["last_name"]
        if self.cleaned_data.get("office", False):
            user.office = self.cleaned_data["office"]
        if self.cleaned_data.get("date_of_birth", False):
            user.date_of_birth = self.cleaned_data["date_of_birth"]
        if self.cleaned_data.get("is_active", False):
            user.is_active = self.cleaned_data["is_active"]
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('office', 'role', 'email', 'first_name', 'last_name', 'date_of_birth', 'password', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]
