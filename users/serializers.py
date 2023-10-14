from rest_framework import serializers

from .models import User, Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['url', 'id', 'title']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'role_id', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'is_active']
