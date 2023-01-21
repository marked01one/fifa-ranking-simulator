from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

from .serializers import ConfederationSerializer, CountrySerializer
from .models import Confederation, Country

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

  
class CountryViewSet(viewsets.ViewSet):
  '''
  API endpoints that allow for accessing country data
  '''
  def list(self, request):
    queryset = Country.objects.all()
    serializer = CountrySerializer(queryset, many=True)
    return Response(serializer.data)
  
  
  '''
  Get all countries from a particular confederation
  '''
  @action(detail=False, url_path='confederation')
  def countries_by_confederation(self, request):
    conf_id = request.query_params['id']
    if conf_id == '1':
      country_queryset = Country.objects.all()
    else:
      country_queryset = Country.objects.filter(confederation=conf_id)
      
    confederation_data = Confederation.objects.filter(id=int(conf_id))
    
    country_serial = CountrySerializer(country_queryset, many=True)
    conf_serial = ConfederationSerializer(confederation_data, many=True)
    
    return Response({
      'confederation': {
        'id': conf_serial.data[0]['id'],
        'name': conf_serial.data[0]['name']
        },
      'countries': country_serial.data
    })
  
  
  '''
  Get country with specific FIFA codename
  '''
  @action(detail=False, url_path='fifa')
  def country_by_fifa_code(self, request):
    
    country = get_object_or_404(Country, fifa_code=request.query_params['code'].upper())
    serializer = CountrySerializer(country)
    
    return Response(serializer.data)
  

class ConfederationViewSet(viewsets.ModelViewSet):
  queryset = Confederation.objects.all()
  serializer_class = ConfederationSerializer