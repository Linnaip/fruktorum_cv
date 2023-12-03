"""Viewsets of the 'api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import permissions, mixins, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializers import (
    CollectionSerializer,
    CreateBookmarkSerializer,
    ReadBookmarkSerializer,
    UrlTypeSerializer,
    UserSerializer,
)
from bookmark.models import Bookmark, Collection, UrlType
from .filters import IsAuthorFilterBackend

User = get_user_model()
PAGINATION = 10

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Вьюсет для юзера."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UrlTypeViewSet(viewsets.ModelViewSet):
    """Вьюсет для Типов Ссылок."""
    queryset = UrlType.objects.all()
    serializer_class = UrlTypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class CollectionViewSet(viewsets.ModelViewSet):
    """Вьюсет для Коллекций"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = (IsAuthorFilterBackend,)
    pagination_class = PageNumberPagination
    pagination_class.page_size = PAGINATION


class BookmarkViewSet(viewsets.ModelViewSet):
    """Вьюсет для Закладок."""
    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer
    filter_backends = (IsAuthorFilterBackend,)
    pagination_class = PageNumberPagination
    pagination_class.page_size = PAGINATION

    def get_serializer_class(self):
        if self.request.method in ("POST", "PATCH"):
            return CreateBookmarkSerializer
        return ReadBookmarkSerializer

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
