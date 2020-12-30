from django.contrib.auth.models import User, Group #change this to reflect our actual models
from fonts.models import FontFamily
from fonts.models import Font
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class FontFamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FontFamily
        fields = ["url", "path_to_font_family", "font_family_name"]


class FontSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Font
        fields = ["font_name"]

