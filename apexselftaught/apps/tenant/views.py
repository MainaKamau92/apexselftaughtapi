from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apexselftaught.apps.core.database import get_model_object
from apexselftaught.apps.tenant.models import Client
from apexselftaught.apps.tenant.renderers import ClientJSONRenderer
from apexselftaught.apps.tenant.serializers import ClientSerializer


class ClientViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    renderer_classes = (ClientJSONRenderer,)
    serializer_class = ClientSerializer

    def create(self, request):
        client = request.data.get('client', {})
        tenant_name = client.get('tenant_name')
        if tenant_name is None:
            raise ValidationError('A tenant name is mandatory.')
        tenant = get_model_object(model=Client, column_name='tenant_name', column_value=tenant_name)
        serializer = self.serializer_class(tenant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
