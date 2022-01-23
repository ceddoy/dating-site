from rest_framework.generics import CreateAPIView, ListAPIView

from clientapp.filters import ClientListFilter
from clientapp.models import Client
from clientapp.permissions import ForNotAuthClientPermission
from clientapp.serializer import CreateClientModelSerializer, ClientListSerializer


class CreateClientAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientModelSerializer
    permission_classes = [ForNotAuthClientPermission, ]


class ClientListView(ListAPIView):
    serializer_class = ClientListSerializer
    filterset_class = ClientListFilter

    def get_queryset(self):
        queryset = Client.objects.all().exclude(id=self.request.user.id)
        return queryset
