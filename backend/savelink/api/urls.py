from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookmarkViewSet, CollectionViewSet, UrlTypeViewSet, UserViewSet

router = DefaultRouter()

router.register(r'books', BookmarkViewSet, basename='books')
router.register(r'collections', CollectionViewSet, basename='collections')
router.register(r'urltype', UrlTypeViewSet, basename='urltype')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
