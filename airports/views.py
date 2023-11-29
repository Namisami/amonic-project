from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.core.files.storage import default_storage
from utils.schedule_import import schedule_import
from rest_framework.decorators import parser_classes

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
        self.queryset = Schedule.objects.all()
        departure = self.request.query_params.get('departure')
        if departure is not None:
            departure_airport = Airport.objects.get(iata_code=departure)
            self.queryset = self.queryset.filter(route__id__in=Route.objects.filter(departure_airport=departure_airport))
        arrival = self.request.query_params.get('arrival')
        if arrival is not None:
            arrival_airport = Airport.objects.get(iata_code=arrival)
            self.queryset = self.queryset.filter(route__id__in=Route.objects.filter(arrival_airport=arrival_airport))
        date = self.request.query_params.get('date')
        if date is not None:
            date_range = self.request.query_params.get('date_range')
            if date_range is not None:
                date
                startdate = datetime.strptime(date, '%Y-%m-%d') - timedelta(days=3)
                enddate = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=3)
                self.queryset = self.queryset.filter(date__range=[startdate, enddate])
            else:
                self.queryset = self.queryset.filter(date=date)
        flight_number = self.request.query_params.get('flight_number')
        if flight_number is not None:
            self.queryset = self.queryset.filter(flight_number=flight_number)
        return self.queryset
    
    @parser_classes([MultiPartParser])
    @action(detail=False, methods=['post'])
    def import_schedule(self, request):
        file = request.data['file']
        file_name = default_storage.save(file.name, file)
        stats = schedule_import(file_name)
        return Response({'message': 'Success', 'successful': stats['successful'], 'duplicate': stats['duplicate'], 'errors': stats['errors']})


class CabinTypeViewSet(viewsets.ModelViewSet):
    queryset = CabinType.objects.all()
    serializer_class = CabinTypeSerializer

    def get_queryset(self):
        self.queryset = CabinType.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = [query for query in self.queryset if str(query.name).lower() == name.lower()]
        return self.queryset


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
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        male_count = Survey.objects.filter(gender='M').count()
        female_count = Survey.objects.filter(gender='F').count()
        age_18_24 = Survey.objects.filter(age__range=(18, 24)).count()
        age_25_39 = Survey.objects.filter(age__range=(25, 39)).count()
        age_40_59 = Survey.objects.filter(age__range=(40, 59)).count()
        age_60 = Survey.objects.filter(age__gte=60).count()
        economy = Survey.objects.filter(travel_class=CabinType.objects.get(name='Economy').id).count()
        business = Survey.objects.filter(travel_class=CabinType.objects.get(name='Business').id).count()
        first = Survey.objects.filter(travel_class=CabinType.objects.get(name='First').id).count()
        auh = Survey.objects.filter(arrival=Airport.objects.get(iata_code='AUH').id).count()
        bah = Survey.objects.filter(arrival=Airport.objects.get(iata_code='BAH').id).count()
        doh = Survey.objects.filter(arrival=Airport.objects.get(iata_code='DOH').id).count()
        ryu = Survey.objects.filter(arrival=Airport.objects.get(iata_code='RUH').id).count()
        cai = Survey.objects.filter(arrival=Airport.objects.get(iata_code='CAI').id).count()
        return Response({
            'male_count': male_count,
            'female_count': female_count,
            'age_18_24': age_18_24,
            'age_25_39': age_25_39,
            'age_40_59': age_40_59,
            'age_60': age_60,
            'economy': economy,
            'business': business,
            'first': first,
            'auh': auh,
            'bah': bah,
            'doh': doh,
            'ryu': ryu,
            'cai': cai
        })


class AmentityViewSet(viewsets.ModelViewSet):
    queryset = Amentity.objects.all()
    serializer_class = AmentitySerializer
        

class AmentityTicketViewSet(viewsets.ModelViewSet):
    queryset = AmentityTicket.objects.all()
    serializer_class = AmentityTicketSerializer
                