from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from clientapp.managers import ClientManager


class Client(AbstractBaseUser, PermissionsMixin):
    SEX_M = 'male'
    SEX_F = 'female'

    STATUS_SEX = (
        (SEX_M, 'мужской'),
        (SEX_F, 'женский'),
    )

    first_name = models.CharField(max_length=64, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия пользователя')
    sex = models.CharField(max_length=9, choices=STATUS_SEX, verbose_name='Пол')

    avatar = models.ImageField(upload_to='client_image', blank=True,
                               default="client_image/default_avatar.jpeg", verbose_name='Аватарка')

    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name='Email')

    is_staff = models.BooleanField(default=False,
                                   help_text='Определяет разрешение пользователя на вход в административную часть.',
                                   verbose_name='Moderator')

    is_active = models.BooleanField(default=True,
                                    help_text='Определяет активен ли пользователь в системе.',
                                    verbose_name='Active')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = ClientManager()

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
