from django.db.models import Q
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from matchapp.models import Like
from matchapp.serializer import ClientToLikeAnotherClient
from clientapp.models import Client
from matchapp.services import get_context_for_mail
from matchapp.tasks import send_email_to_users
# from matchapp.services import send_email_to_users


class MatchClientsRetrieveView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientToLikeAnotherClient

    # Процесс отработки при клики "Мне нравится"
    def put(self, request, *args, **kwargs):
        from_like_user = Like.objects.create(from_like_user_id=request.user.id, to_like_user_id=kwargs.get('pk'))
        to_like_user = Like.objects.filter(Q(from_like_user_id=kwargs.get('pk')) &
                                           Q(to_like_user_id=request.user.id)).select_related('from_like_user').first()
        if to_like_user:
            send_email_to_users.delay(get_context_for_mail(to_like_user.from_like_user), get_context_for_mail(request.user))
            self.request.data['email'] = to_like_user.from_like_user.email
            serializer = self.get_serializer(to_like_user.from_like_user, data=request.data)
        else:
            serializer = self.get_serializer(from_like_user.to_like_user, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.data.get('email'):
            context.update({'email': self.request.data.get('email')})
        return context
