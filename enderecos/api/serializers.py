from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from ..models import Endereco

class EnderecoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Endereco
        geo_field = "location"
        fields = ('id', 'location')