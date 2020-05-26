from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from core.mixins import MixedPermissionModelViewSet
from ..models import Avaliacao

from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(MixedPermissionModelViewSet):
    queryset = Avaliacao.objects.all()
    authentication_classes = (TokenAuthentication, )

    serializer_class = AvaliacaoSerializer

    permission_classes_by_action = {'create': [IsAuthenticated], 'list': [AllowAny], 'patch': [IsAuthenticated], 'destroy': [IsAuthenticated]}

    def create(self, request, *args, **kwargs):
        copy_data = request.data.copy()
        copy_data['user'] = request.auth.user.id

        serializer = self.get_serializer(data=copy_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.user_id is not request.auth.user.id:
            return Response({'detail': 'Não é possível atualizar uma avaliação da qual você não é dono'}, status=status.HTTP_403_FORBIDDEN)

        return super(AvaliacaoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if (instance.user_id is not request.auth.user.id) and not IsAdminUser:
            return Response({'detail': 'Apenas o dono da avaliação ou administradores podem exlui-la'}, status=status.HTTP_403_FORBIDDEN)

        super(AvaliacaoViewSet, self).destroy(request, *args, **kwargs)
        return Response({'message': 'avaliação excluida com sucesso'})


