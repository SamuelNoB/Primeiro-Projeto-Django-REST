from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.mixins import MixedPermissionModelViewSet
from ..models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(MixedPermissionModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    authentication_classes = (TokenAuthentication, )
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'patch': [IsAuthenticated],
                                    'destroy': [IsAuthenticated]}

    filter_fields = ('name', 'description')

    def create(self, request, *args, **kwargs):
        return super(AtracaoViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(AtracaoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        super(AtracaoViewSet, self).destroy(request, *args, **kwargs)
        return Response({'detail': 'aAtração deletada com sucesso'})