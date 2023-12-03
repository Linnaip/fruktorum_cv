from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Никнейм'
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Почта'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
