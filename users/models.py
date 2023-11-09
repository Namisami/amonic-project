from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class Role(models.Model):
    title = models.CharField(verbose_name='Роль', max_length=255)
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title
    

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Office(models.Model):
    country = models.ForeignKey(verbose_name='Страна', to=Country, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+7**********'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Телефонный номер', blank=True)
    contact = models.CharField(max_length=255, verbose_name='Контакты', blank=True)

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return self.title


class User(AbstractUser):
    username = None
    office = models.ForeignKey(verbose_name='Офис', to=Office, on_delete=models.PROTECT, null=True)
    role = models.ForeignKey(verbose_name='Роль', to=Role, on_delete=models.PROTECT, null=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='Имя', blank=True, max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', blank=True, max_length=255)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
    last_logout = models.DateTimeField(verbose_name='Время выхода', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def online_time(self):
        if self.last_login < self.last_logout:
            return 0
        else:
            return timezone.now() - self.last_login
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.email

@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    user.last_logout = timezone.now()
    user.save()
