from django.db import models

from clientapp.models import Client


class Like(models.Model):
    from_like_user = models.ForeignKey(Client, on_delete=models.CASCADE,
                                       verbose_name='Пользователь',
                                       related_name='like_user_from')
    to_like_user = models.ForeignKey(Client, on_delete=models.CASCADE,
                                     blank=True,
                                     verbose_name='Нравится',
                                     related_name='like_user_to')

    class Meta:
        verbose_name = 'Нравится'
        verbose_name_plural = 'Нравятся'
