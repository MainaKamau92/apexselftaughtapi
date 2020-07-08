from storages.backends.gcloud import GoogleCloudStorage
from tenant_schemas.storage import TenantStorageMixin


class TenantGoogleCloudStorage(TenantStorageMixin, GoogleCloudStorage):
    pass
