from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

from .managers import CustomUserManager


class Role(models.Model):
    title = models.CharField(verbose_name='Роль', max_length=255)
    
    @classmethod
    def get_default_pk(cls):
        role, created = cls.objects.get_or_create(title='Пользователь')
        return role.pk
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class User(AbstractUser):
    username = None
    # office_id
    role_id = models.ForeignKey(verbose_name='Роль', to=Role, on_delete=models.PROTECT, default=Role.get_default_pk)
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='Имя', blank=True, max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', blank=True, max_length=255)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
    last_logout = models.DateTimeField(verbose_name='Время выхода')

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
