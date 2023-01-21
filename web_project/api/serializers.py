from django.contrib.auth.models import User, Group
from api.models import Confederation, Country
from rest_framework import serializers


# Authorization level
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')
    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')


# Serializers
class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ('id', 'full_name', 'fifa_code', 'flag_url', 'confederation')
    

class ConfederationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Confederation
    fields = ('id', 'name')