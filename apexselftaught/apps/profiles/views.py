from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from apexselftaught.apps.core.database import get_query_set, get_model_object
from apexselftaught.apps.core.permissions import IsOwnerOnly
from apexselftaught.apps.profiles.models import Profile
from apexselftaught.apps.profiles.renderers import ProfileJSONRenderer
from apexselftaught.apps.profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser,)

    def list(self, request):
        queryset = get_query_set(Profile)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        profile = get_model_object(model=Profile, column_name="id", column_value=pk)
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        profile = request.data
        profile_instance = get_model_object(model=Profile, column_name="id", column_value=pk)
        self.check_object_permissions(request, profile_instance)
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(instance=profile_instance,
                                           data=profile, context=serializer_context,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
