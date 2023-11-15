from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import UserSerializer, RoleSerializer, OfficeSerializer, CountrySerializer, ErrorSerializer, VisitSerializer
from .models import User, Role, Office, Country, Error, Visit


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title is not None:
            self.queryset = [query for query in self.queryset if str(query.title).lower() == title.lower()]
        return self.queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
