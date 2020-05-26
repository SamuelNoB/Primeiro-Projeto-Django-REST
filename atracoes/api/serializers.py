from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField

from ..models import Atracao
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class AtracaoSerializer(ModelSerializer):
    point = PrimaryKeyRelatedField(many=False, queryset=PontoTuristico.objects.all())


    class Meta:
        model = Atracao
        fields = ('id', 'point', 'name', 'photo', 'description', 'opening_hours', 'min_age')

    def create(self, validated_data):
            ponto_turistico_data = validated_data.pop('point')
            ponto_turistico = PontoTuristico.objects.get(pk=ponto_turistico_data['id'])
            atracao = Atracao.objects.create(point=ponto_turistico, **validated_data)
            return atracao
