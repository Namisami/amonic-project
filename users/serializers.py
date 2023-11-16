from rest_framework import serializers

from .models import User, Role, Office, Country, Error, Visit


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['url', 'id', 'title']


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['url', 'id', 'name']


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ['url', 'id', 'country', 'title', 'phone', 'contact']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    online_time = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['url', 'id', 'office', 'role', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'online_time', 'last_login', 'last_logout', 'crushes_count']
        depth = 1


class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['office', 'role', 'email', 'first_name', 'last_name', 'date_of_birth']


class ErrorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Error
        fields = ['url', 'id', 'user', 'description', 'reason']
        depth = 1


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = ['url', 'id', 'user', 'error']
        depth = 1
        