from django.core.validators import RegexValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Office(models.Model):
    country_id = models.ForeignKey(to=Country, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Название')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+7**********'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Телефонный номер', blank=True)
    contact = models.CharField(max_length=255, verbose_name='Контакты', blank=True)

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return self.title
