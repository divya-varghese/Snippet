from django.urls import path
from rest_framework import routers

from core.views import ContentViewSet,TagViewSet
router = routers.DefaultRouter()
router.register(r'snippet', ContentViewSet)
router.register(r'tags', TagViewSet,basename='tags')