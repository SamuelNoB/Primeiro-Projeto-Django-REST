from django.contrib.auth.models import User
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField

from core.models import PontoTuristico
from ..models import Comentario


class ComentarioSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    point = PrimaryKeyRelatedField(many=False, queryset=PontoTuristico.objects.all())

    class Meta:
        model = Comentario
        fields = ('id', 'user', 'point', 'comment', 'approved', 'created_at', 'updated_at')
