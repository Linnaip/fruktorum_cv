from rest_framework import filters


class IsAuthorFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated:
            return queryset.filter(user=request.user)
        else:
            return queryset.none()
