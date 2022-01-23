from rest_framework.serializers import ModelSerializer

from clientapp.models import Client


class ClientToLikeAnotherClient(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', "avatar")

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        if self.context.get('email', False):
            instance['email'] = self.context.get('email')
        return instance
