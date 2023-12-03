from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_LENGTH = 256


class UrlType(models.Model):
    """
    Класс типа ссылки.
    """

    name = models.CharField(
        "Тип ссылки",
        max_length=MAX_LENGTH
    )

    class Meta:
        verbose_name = "Тип ссылки"
        verbose_name_plural = "Тип ссылок"

    def __str__(self):
        return self.name


class Collection(models.Model):
    """
    Класс коллекции.
    """
    name = models.CharField(
        "Название коллекции",
        unique=True,
        max_length=MAX_LENGTH,
    )
    description = models.CharField(
        "Описание коллекции",
        max_length=MAX_LENGTH,
    )
    time_created = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
    )
    time_updated = models.DateTimeField(
        "Дата обновления",
        auto_now=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collections'
    )

    class Meta:
        verbose_name = "коллекция"
        verbose_name_plural = "коллекции"

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    """
    Класс для закладок.
    """

    title = models.CharField(
        "Заголовок",
        max_length=MAX_LENGTH,
    )
    description = models.CharField(
        "Описание",
        max_length=MAX_LENGTH,
        blank=True,
        null=True,
    )
    url = models.URLField(
        "Ссылка",
    )
    url_type = models.ForeignKey(
        UrlType,
        verbose_name="Тип ссылки",
        on_delete=models.PROTECT,
        related_name="bookmarks",
        default=1,
    )
    image = models.ImageField(
        "image",
        max_length=MAX_LENGTH,
        upload_to="savelink/images/",
    )
    time_created = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
    )
    time_updated = models.DateTimeField(
        "Дата обновления",
        auto_now=True,
    )
    collections = models.ManyToManyField(
        Collection,
        verbose_name="Коллекция",
        related_name="bookmarks",
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )

    class Meta:
        verbose_name = "Закладка"
        verbose_name_plural = "Закладки"

    def __str__(self):
        return self.title
