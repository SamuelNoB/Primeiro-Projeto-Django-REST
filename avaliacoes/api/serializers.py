from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField

from core.models import PontoTuristico
from ..models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    point = PrimaryKeyRelatedField(many=False, queryset=PontoTuristico.objects.all())

    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'point', 'comment', 'rate', 'created_at', 'updated_at')