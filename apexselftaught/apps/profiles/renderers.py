from apexselftaught.apps.core.renderers import ApexJSONRenderer


class ProfileJSONRenderer(ApexJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profile_count'
