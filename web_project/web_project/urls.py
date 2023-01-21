"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from email.mime import base
from rest_framework import routers
from django.urls import include, path
from api import views

# countries = views.CountryViewSet.as_view({'get': 'list'})
# countries_by_confederation = views.CountryViewSet.as_view({'get': 'retrieve'})

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('countries', views.CountryViewSet, basename='Country')
# router.register('countries/retrieve_conf/<int:pk>', views.CountryViewSet.as_view({'get': 'retrieve_confederation'}), basename='Country')
# router.register('countries/retrieve_by_fifa/<str:pk>', views.CountryViewSet.as_view({'get': 'retrieve_country_by_fifa_code'}), basename='Country')
router.register('confederations', views.ConfederationViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
