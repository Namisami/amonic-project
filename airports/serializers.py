from rest_framework import serializers

from .models import Country, Office, Aircraft, Airport, Schedule, Route


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['url', 'id', 'name']


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ['url', 'id', 'country', 'title', 'phone', 'contact']


class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airport
        fields = ['url', 'id', 'country', 'iata_code', 'name']


class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['url', 'id', 'name', 'make_model', 'total_seats', 'economy_seats', 'business_seats']


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ['url', 'id', 'departure_airport', 'arrival_airport', 'distance', 'flight_time']
        

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['url', 'id', 'date', 'time', 'aircraft', 'route', 'flight_number', 'economy_price', 'confirmed']
