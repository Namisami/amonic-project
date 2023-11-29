from rest_framework import serializers

from .models import Aircraft, Airport, Schedule, Route, CabinType, Ticket, Survey, Amentity, AmentityTicket


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
        fields = ['url', 'id', 'date', 'time', 'aircraft', 'route', 'flight_number', 'economy_price', 'business_price', 'first_class_price', 'confirmed']
        depth = 2
        

class CabinTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CabinType
        fields = ['url', 'id', 'name']
        

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        super(TicketSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
    class Meta:
        model = Ticket
        fields = ['url', 'id', 'user', 'schedule', 'cabin_type', 'first_name', 'last_name', 'email', 'phone', 'passport_number', 'passport_country', 'booking_reference', 'confirmed', 'departure_airport', 'arrival_airport', 'outbound', 'return_date']
        depth = 3


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['url', 'id', 'departure', 'arrival', 'age', 'gender', 'travel_class', 'q1', 'q2', 'q3', 'q4']
        # fields = '__all__'


class AmentitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amentity
        fields = ['url', 'id', 'service', 'price']


class AmentityTicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmentityTicket
        fields = ['url', 'id', 'amentity', 'ticket', 'price']
