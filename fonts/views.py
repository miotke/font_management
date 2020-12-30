from django.shortcuts import render
from django.contrib.auth.models import User #Again, change this model to reflect actual usage
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from fonts.serializers import UserSerializer
from fonts.serializers import GroupSerializer
from fonts.serializers import FontFamilySerializer
from fonts.serializers import FontSerializer
from fonts.models import FontFamily
from fonts.models import Font

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


class FontViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows font families to be viewed or edited.
    """
    queryset = Font.objects.all()
    serializer_class = FontSerializer
    permission_class = [permissions.IsAuthenticated]
