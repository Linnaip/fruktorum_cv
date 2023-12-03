from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from bookmark.models import Bookmark, Collection, UrlType
from api.utilits import get_info
from users.models import User


class CreateUsersSerializer(UserCreateSerializer):
    """Для создания юзера."""
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password'
        )
        extra_kwargs = {
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(UserSerializer):
    """Отображение пользователя."""
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username'
        )


class UrlTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name",)
        model = UrlType


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "description",
            "time_created",
            "time_updated",
        )
        model = Collection

    def create(self, validated_data):
        user_data = self.context.get("request").user
        collection = Collection.objects.create(
            user=user_data, **validated_data
        )
        return collection


class CreateBookmarkSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Collection.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        fields = (
            "url",
            "time_created",
            "time_updated",
            "collections",
        )
        model = Bookmark

    def create(self, validated_data):
        user_data = self.context.get("request").user
        collection_data = validated_data.pop('collections', [])
        url_data = validated_data['url']
        link_data = get_info(url_data)
        type_data = link_data['url_type']
        if type_data in None:
            url_type = UrlType.objects.get(name='website')
        title = link_data['title']
        description = link_data['description']
        image = link_data['image']
        
        bookmark = Bookmark.objects.create(
            user=user_data,
            url_type_id=url_type.id,
            title=title,
            description=description,
            image=image,
            **validated_data
        )
        existing_collections = Collection.objects.filter(
            name__in=collection_data
        )
        bookmark.collections.set(existing_collections)
        bookmark.save()

    def to_representation(self, instance):
        return ReadBookmarkSerializer(instance, context=self.context).data


class ReadBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = (
            "title",
            "description",
            "url",
            "url_type",
            "image",
            "time_created",
            "time_updated",
            "collections",
        )
