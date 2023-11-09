from django.db import models
import math

from users.models import User, Country
    

class Airport(models.Model):
    country = models.ForeignKey(verbose_name='Страна', to=Country, on_delete=models.PROTECT, null=True)
    iata_code = models.CharField(verbose_name='Код аэропорта', max_length=3)
    name = models.CharField(verbose_name='Название', max_length=255, blank=True)

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
    make_model = models.CharField(verbose_name='Марка', max_length=255, blank=True)
    total_seats = models.PositiveIntegerField(verbose_name='Количество сидений', null=True)
    economy_seats = models.PositiveIntegerField(verbose_name='Мест в экономе', null=True)
    business_seats = models.PositiveIntegerField(verbose_name='Мест в бизнес-классе', null=True)

    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

    def __str__(self):
        return self.make_model + ' ' + self.name
    

class Schedule(models.Model):
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    aircraft = models.ForeignKey(verbose_name='Самолет', to=Aircraft, on_delete=models.PROTECT)
    route = models.ForeignKey(verbose_name='Рейс', to=Route, on_delete=models.PROTECT)
    flight_number = models.CharField(verbose_name='Номер рейса', max_length=255)
    economy_price = models.PositiveIntegerField(verbose_name='Стоимость эконома')
    confirmed = models.BooleanField(verbose_name='Наличие подтверждения', default=True)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return self.flight_number + ' ' + str(self.route)

    @property
    def business_price(self):
        price = math.ceil(self.economy_price * 1.35)
        return price
    
    @property
    def first_class_price(self):
        price = math.ceil(self.economy_price * 1.35 * 1.3)
        return price
    

class CabinType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Тип кабины'
        verbose_name_plural = 'Типы кабин'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.PROTECT)
    schedule = models.ForeignKey(verbose_name='Рейс', to=Schedule, on_delete=models.PROTECT)
    cabin_type = models.ForeignKey(verbose_name='Тип кабины', to=CabinType, on_delete=models.PROTECT)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Номер телефона', max_length=255)
    passport_number = models.CharField(verbose_name='Номер паспорта', max_length=255)
    passport_country = models.ForeignKey(verbose_name='Гражданство', to=Country, on_delete=models.PROTECT)
    booking_reference = models.CharField(verbose_name='Номер брони', max_length=255)
    confirmed = models.BooleanField(verbose_name='Наличие подтверждения')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.booking_reference}'
    
    @property
    def departure_airport(self):
        route_id = Schedule.objects.get(id=self.schedule.id).route.id
        route = Route.objects.get(id=route_id)
        return route.departure_airport.iata_code
    
    @property
    def arrival_airport(self):
        route_id = Schedule.objects.get(id=self.schedule.id).route.id
        route = Route.objects.get(id=route_id)
        return route.arrival_airport.iata_code
    
    @property
    def outbound(self):
        date = Schedule.objects.get(id=self.schedule.id).date
        return date
    
    @property
    def return_date(self):
        user_tickets = Ticket.objects.filter(user=self.user)
        route_id = Route.objects.get(arrival_airport=Airport.objects.get(iata_code=self.departure_airport)).id
        schedule = Schedule.objects.get(id=self.schedule.id)
        return_schedules = Schedule.objects.filter(route=route_id, date__gte=schedule.date, time__gt=schedule.time)
        if return_schedules.count() > 0:
            return_tickets = user_tickets.filter(schedule=return_schedules[0])
            return_schedule = Schedule.objects.get(id=return_tickets[0].schedule.id)
            return return_schedule.date
        return None
    

class Survey(models.Model):
    departure = models.ForeignKey(verbose_name='Откуда', to=Airport, on_delete=models.PROTECT, related_name='departure', null=True)
    arrival = models.ForeignKey(verbose_name='Куда', to=Airport, on_delete=models.PROTECT, related_name='arrival', null=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
    gender = models.CharField(verbose_name='Пол', max_length=2, default='NS', blank=True, null=True)
    travel_class = models.ForeignKey(verbose_name='Класс билета', to=CabinType, on_delete=models.PROTECT, null=True)
    q1 = models.IntegerField(verbose_name='Оценка самолета', default=0, null=True)
    q2 = models.IntegerField(verbose_name='Оценка проводников', default=0, null=True)
    q3 = models.IntegerField(verbose_name='Оценка развлечений', default=0, null=True)
    q4 = models.IntegerField(verbose_name='Оценка стоимости', default=0, null=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.departure} -> {self.arrival}'
    

class Amentity(models.Model):
    service = models.CharField(verbose_name='Название', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Доп. услуга'
        verbose_name_plural = 'Доп. услуги'

    def __str__(self):
        return self.service
    

class AmentityTicket(models.Model):
    amentity = models.ForeignKey(verbose_name='Доп. услуга', to=Amentity, on_delete=models.PROTECT)
    ticket = models.ForeignKey(verbose_name='Билет', to=Ticket, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Билет с услугой'
        verbose_name_plural = 'Билеты с услугами'

    def __str__(self):
        return str(self.ticket)
