from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import viewsets_phone,viewsets_ratings

router= routers.DefaultRouter()
router.register('phones',viewsets_phone)
router.register('ratings',viewsets_ratings)

urlpatterns = [
    path('',include(router.urls))
]