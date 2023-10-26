from rest_framework import viewsets

from .serializers import CountrySerializer, OfficeSerializer, AircraftSerializer, AirportSerializer, RouteSerializer, ScheduleSerializer
from .models import Country, Office, Aircraft, Airport, Route, Schedule


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    ordering_fields = ['date', 'time', 'economy_price', 'confirmed']

    def get_queryset(self):
        departure = self.request.query_params.get('departure')
        if departure is not None:
            queryset = queryset.filter(departure_airport=departure)
        arrival = self.request.query_params.get('arrival')
        if arrival is not None:
            queryset = queryset.filter(arrival_airport=arrival)
        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(date=date)
        flight_number = self.request.query_params.get('flight_number')
        if flight_number is not None:
            queryset = queryset.filter(flight_number=flight_number)
