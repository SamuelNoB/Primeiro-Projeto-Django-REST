# from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import EnderecoSerializer
from core.mixins import MixedPermissionModelViewSet
from ..models import Endereco

class EnderecoViewSet(MixedPermissionModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    authentication_classes = (TokenAuthentication, )
    permission_classes_by_action =  {
        'create': [IsAuthenticated],
        'patch': [IsAuthenticated],
        'destroy': [IsAuthenticated]
    }

    def create(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).destroy(request, *args, **kwargs)





