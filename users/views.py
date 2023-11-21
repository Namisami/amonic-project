from django.utils import timezone
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


from .serializers import UserSerializer, UserPostSerializer, RoleSerializer, OfficeSerializer, CountrySerializer, ErrorSerializer, VisitSerializer, ErrorPostSerializer
from .models import User, Role, Office, Country, Error, Visit


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        user = User.objects.get(email=request.data['email'])
        user.last_login = timezone.now()
        user.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    authentication_classes = [JWTAuthentication]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [JWTAuthentication]


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title is not None:
            self.queryset = [query for query in self.queryset if str(query.title).lower() == title.lower()]
        return self.queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = UserPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user is not None:
            self.queryset = [query for query in self.queryset if str(query.user.id) == user]
        return self.queryset
    
    def create(self, request, *args, **kwargs):
        serializer = ErrorPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        self.queryset = Visit.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            self.queryset = [query for query in self.queryset if str(query.user.id) == user]
        return self.queryset
    
    def update(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=self.get_object())
            error = Error.objects.get(id=request.data['error'])
            instance = Visit.objects.filter(user=user.id).order_by('-id')[0]
            instance.error = error
            instance.save()
            return Response({'message': 'Success'})
        except Exception as e:
            return Response({'message': 'Error'})
        

@authentication_classes([JWTAuthentication])
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Success'})
