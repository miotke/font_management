from django.urls import include
from django.urls import path
from rest_framework import routers
from . import views

# For new URL endpoints, add register a new router below.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"font-family", views.FontFamilyViewSet)

urlpatterns = [
        path("", include(router.urls)),
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
