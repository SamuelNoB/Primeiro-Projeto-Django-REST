from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from enderecos.models import Endereco
from ..models import PontoTuristico

from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao


class PontoTuristicoSerializer(serializers.ModelSerializer):

    attractions = serializers.StringRelatedField(many=True, read_only=True)


    address = EnderecoSerializer(many=False)
    complete_description = SerializerMethodField()  # serve para retornar um campo customizado

    def get_complete_description(self, obj):
        return '%s - %s ' % (obj.name, obj.description)

    class Meta:
        model = PontoTuristico
        fields = ['id', 'name', 'photo', 'attractions', 'description', 'address', 'complete_description', 'complete_description2']

    def create(self, validated_data):

        address_data = validated_data.pop('address')
        address = Endereco.objects.create(**address_data)
        ponto_turistico = PontoTuristico.objects.create(address=address, **validated_data)

        return ponto_turistico



class UserSerializer(serializers.ModelSerializer):

    full_name = SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'first_name', 'last_name', 'email']