from rest_framework import viewsets

from .serializers import AircraftSerializer, AirportSerializer, RouteSerializer, ScheduleSerializer, CabinTypeSerializer, TicketSerializer, SurveySerializer, AmentitySerializer, AmentityTicketSerializer
from .models import Aircraft, Airport, Route, Schedule, CabinType, Ticket, Survey, Amentity, AmentityTicket


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
            self.queryset = self.queryset.filter(departure_airport=departure)
        arrival = self.request.query_params.get('arrival')
        if arrival is not None:
            self.queryset = self.queryset.filter(arrival_airport=arrival)
        date = self.request.query_params.get('date')
        if date is not None:
            self.queryset = self.queryset.filter(date=date)
        flight_number = self.request.query_params.get('flight_number')
        if flight_number is not None:
            self.queryset = self.queryset.filter(flight_number=flight_number)
        return self.queryset


class CabinTypeViewSet(viewsets.ModelViewSet):
    queryset = CabinType.objects.all()
    serializer_class = CabinTypeSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        cabin_type = self.request.query_params.get('cabin_type')
        if cabin_type is not None:
            self.queryset = self.queryset.filter(cabin_type=cabin_type)
        arrival_airport = self.request.query_params.get('arrival_airport')
        if arrival_airport is not None:
            self.queryset = [query for query in self.queryset if query.arrival_airport == arrival_airport]
        departure_airport = self.request.query_params.get('departure_airport')
        if departure_airport is not None:
            self.queryset = [query for query in self.queryset if query.departure_airport == departure_airport]
        outbound = self.request.query_params.get('outbound')
        if outbound is not None:
            self.queryset = [query for query in self.queryset if str(query.outbound) == outbound]
        return_date = self.request.query_params.get('return_date')
        if return_date is not None:
            self.queryset = [query for query in self.queryset if str(query.return_date) == return_date]
        return self.queryset
        

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
        

class AmentityViewSet(viewsets.ModelViewSet):
    queryset = Amentity.objects.all()
    serializer_class = AmentitySerializer
        

class AmentityTicketViewSet(viewsets.ModelViewSet):
    queryset = AmentityTicket.objects.all()
    serializer_class = AmentityTicketSerializer
                