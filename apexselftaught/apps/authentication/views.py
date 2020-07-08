from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework.response import Response
from apexselftaught.apps.core.database import get_model_object, get_query_set
from apexselftaught.apps.core.send_email import send_password_reset_link
from apexselftaught.apps.authentication.serializers import (RegistrationSerializer, LoginSerializer,
                                                            ResetPasswordRequestSerializer, ResetPasswordSerializer)
from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.core.utils import jwt_decode
from apexselftaught.apps.authentication.renderers import UserJSONRenderer


class RegistrationViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def create(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = get_query_set(User)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


class EmailVerificationView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)

    @staticmethod
    def get(request, token):
        try:
            payload = jwt_decode(token=token)
            user = get_model_object(model=User, column_name="username", column_value=payload.get("user"))
            user.is_verified = True
            user.save()
            return Response(dict(message="Email verified successfully"), status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(dict(error="User with that id does not exist"), status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PasswordResetRequestView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        send_password_reset_link(serializer.data)
        return Response({"message": "Instructions on how to reset password have been sent to your email."},
                        status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ResetPasswordSerializer

    def patch(self, request, token):
        payload = jwt_decode(token=token)
        user = get_model_object(model=User, column_name="username", column_value=payload.get("user"))
        password_data = request.data.get('user', {})
        serializer = self.serializer_class(data=password_data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(dict(message="Password reset successfully"), status=status.HTTP_200_OK)
