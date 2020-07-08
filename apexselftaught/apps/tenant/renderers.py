from apexselftaught.apps.core.renderers import ApexJSONRenderer


class ClientJSONRenderer(ApexJSONRenderer):
    object_label = 'client'
    pagination_object_label = 'clients'
    pagination_count_label = 'clientCount'
