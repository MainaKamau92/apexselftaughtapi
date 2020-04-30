from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apexselftaught.apps.authentication.views import RegistrationViewSet, EmailVerificationView, LoginView, \
    PasswordResetRequestView, PasswordResetView

router = DefaultRouter(trailing_slash=False)
router.register(r'users', RegistrationViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path("verify-email/<str:token>", EmailVerificationView.as_view(), name="verify-email"),
    path("login/", LoginView.as_view(), name="login"),
    path("password-reset-request/", PasswordResetRequestView.as_view(), name="password-reset-request"),
    path("password-reset/<str:token>", PasswordResetView.as_view(), name="reset-password")
]
