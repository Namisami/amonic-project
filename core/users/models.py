from django.db import models
from django.contrib.auth.models import AbstractUser

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
    role_id = models.ForeignKey(to=Role, on_delete=models.PROTECT, default=Role.get_default_pk)
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='Имя', blank=True, max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', blank=True, max_length=255)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.email

