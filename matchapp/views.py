from rest_framework.generics import RetrieveUpdateAPIView

from matchapp.models import Like
from matchapp.serializer import ClientToLikeAnotherClient
from clientapp.models import Client
from matchapp.services import send_email_to_users


class MatchClientsRetrieveView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientToLikeAnotherClient

    # Процесс отработки при клики "Мне нравится"
    def put(self, request, *args, **kwargs):
        user_likes = Client.objects.get(id=kwargs['pk'])
        like = Like.objects.get_or_create(like_user=user_likes)
        Like.objects.get_or_create(like_user=request.user)
        request.user.likes.add(like[0])
        if user_likes.likes.filter(id=Like.objects.get(like_user=request.user).id):
            send_email_to_users(user_likes, request.user)
            self.request.data['email'] = user_likes.email
        return self.update(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.data.get('email'):
            context.update({'email': self.request.data.get('email')})
        return context
