from tenant_schemas.middleware import BaseTenantMiddleware
from tenant_schemas.utils import get_public_schema_name


class RequestIDTenantMiddleware(BaseTenantMiddleware):

    def get_tenant(self, model, hostname, request):
        public_schema = model.objects.get(schema_name=get_public_schema_name())

        x_request_id = request.META.get('HTTP_X_REQUEST_ID', public_schema.tenant_uuid)
        # import pdb;
        # pdb.set_trace()
        tenant_model = model.objects.get(tenant_uuid=x_request_id)
        print(tenant_model, public_schema)
        return tenant_model if not None else public_schema
