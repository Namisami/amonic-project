from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import UserSerializer, RoleSerializer
from .models import User, Role


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
