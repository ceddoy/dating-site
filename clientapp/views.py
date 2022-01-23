from rest_framework.generics import CreateAPIView

from clientapp.models import Client
from clientapp.permissions import ForNotAuthClientPermission
from clientapp.serializer import CreateClientModelSerializer


class CreateClientAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientModelSerializer
    permission_classes = [ForNotAuthClientPermission, ]
