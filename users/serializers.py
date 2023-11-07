from rest_framework import serializers

from .models import User, Role, Office, Country


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
        fields = ['url', 'id', 'office', 'role', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'online_time', 'last_logout']
