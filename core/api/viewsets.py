from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..mixins import MixedPermissionModelViewSet
from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer, UserSerializer


class UserViewset(MixedPermissionModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )

    permission_classes_by_action = {'partial_update': [IsAuthenticated],
                                    'list': [IsAdminUser]}

    def list(self, request, *args, **kwargs):
        return super(UserViewset, self).list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        valor = super(UserViewset, self).partial_update(request, *args, **kwargs)
        return valor


class PontoTuristicoViewset(MixedPermissionModelViewSet):

    serializer_class = PontoTuristicoSerializer

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'patch': [IsAuthenticated],
                                    'destroy': [IsAuthenticated]}

    authentication_classes = (TokenAuthentication,)

    filter_backends = (SearchFilter, )
    search_fields = ('name', 'description', 'attractions__name', 'adress__city')
    lookup_field = 'name'  # altera o parametro padrão de recebimento -> pontoturistico/<nome do objeto> -> nome do objeto deve ser único

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = PontoTuristico.objects.all()

        if id:
            return queryset.filter(pk=id)

        if name:
            queryset = queryset.filter(name__iexact=name)

        if description:
            queryset = queryset.filter(description__iexact=description)

        return queryset

    @action(methods=['patch'], detail=True)
    def denunciar(self, request, pk=None):
        request.data['name'] = 'denunciado'
        self.update(request)
        return Response({'message': 'o ponto foi denunciado', 'name': request.data['name']})


# metodos que podem ser sobrescritos no rest framework para uma ação personalizada
#    def list(self, request, *args, **kwargs):
#    def create(self, request, *args, **kwargs):
#    def retrieve(self, request, *args, **kwargs):
#    def destroy(self, request, *args, **kwargs):
#    def update(self, request, *args, **kwargs):
#    def partial_update(self, request, *args, **kwargs):
