from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apexselftaught.apps.tenant.views import ClientViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'client', ClientViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
