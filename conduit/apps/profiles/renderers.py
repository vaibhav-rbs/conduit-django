from conduit.apps.core.renderers import ConduitJSONRenderer

class ProfileJSONRenderer(ConduitJSONRenderer):
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'