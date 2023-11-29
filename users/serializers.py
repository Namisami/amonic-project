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
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
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


class ErrorPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Error
        fields = ['url', 'id', 'user', 'description', 'reason']


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        super(VisitSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2
    class Meta:
        model = Visit
        fields = ['url', 'id', 'user', 'error', 'login_time', 'logout_time']
        depth = 2


class VisitPostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(required=False)
    login_time = serializers.ReadOnlyField(required=False)
    class Meta:
        model = Visit
        fields = ['url', 'id', 'user', 'error', 'login_time', 'logout_time']
        