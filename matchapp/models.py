from django.db import models

from clientapp.models import Client


class Like(models.Model):
    like_user = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Пользователи', related_name='like')

    class Meta:
        verbose_name = 'Нравится'
        verbose_name_plural = 'Нравятся'

    def __str__(self):
        return f"{self.like_user}"
