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
    country = models.ForeignKey(verbose_name='Страна', to=Country, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Название')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+7**********'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Телефонный номер', blank=True)
    contact = models.CharField(max_length=255, verbose_name='Контакты', blank=True)

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return self.title
    

class Airport(models.Model):
    country = models.ForeignKey(verbose_name='Страна', to=Country, on_delete=models.PROTECT)
    iata_code = models.CharField(verbose_name='Код аэропорта', max_length=3)
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'

    def __str__(self):
        return self.iata_code


class Route(models.Model):
    departure_airport = models.ForeignKey(verbose_name='Аэропорт отправления', to=Airport, on_delete=models.PROTECT, related_name='departure_airport')
    arrival_airport = models.ForeignKey(verbose_name='Аэропорт прибытия', to=Airport, on_delete=models.PROTECT, related_name='arrival_airport')
    distance = models.PositiveIntegerField(verbose_name='Дистанция полета')
    flight_time = models.PositiveIntegerField(verbose_name='Время полета')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return str(self.departure_airport) + ' -> ' + str(self.arrival_airport)


class Aircraft(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    make_model = models.CharField(verbose_name='Марка', max_length=255)
    total_seats = models.PositiveIntegerField(verbose_name='Количество сидений')
    economy_seats = models.PositiveIntegerField(verbose_name='Мест в экономе')
    business_seats = models.PositiveIntegerField(verbose_name='Мест в бизнес-классе')

    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

    def __str__(self):
        return self.make_model + ' ' + self.name
    

class Schedule(models.Model):
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    aircraft = models.ForeignKey(to=Aircraft, on_delete=models.PROTECT)
    route = models.ForeignKey(to=Route, on_delete=models.PROTECT)
    flight_number = models.CharField(verbose_name='Номер рейса', max_length=255)
    economy_price = models.PositiveIntegerField(verbose_name='Стоимость эконома')
    confirmed = models.BooleanField(verbose_name='Наличие подтверждения')

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return self.flight_number + ' ' + str(self.flight_number)
