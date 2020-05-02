from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apexselftaught.apps.profiles.views import ProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]
