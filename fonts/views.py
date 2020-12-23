from django.shortcuts import render
from django.contrib.auth.models import User, Group #Again, change this model to reflect actual usage
from rest_framework import viewsets
from rest_framework import permissions
from fonts.serializers import UserSerializer, GroupSerializer, FontFamilySerializer
from fonts.models import FontFamily

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited. 
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permissions_class = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_class = [permissions.IsAuthenticated]


class FontFamilyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows font families to be viewed or edited.
    """
    queryset = FontFamily.objects.all()
    serializer_class = FontFamilySerializer
    permission_class = [permissions.IsAuthenticated]

