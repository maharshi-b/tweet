from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultsPagination


class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        following_users = self.request.user.profile.get_following()
        qs = Tweet.objects.filter(
            Q(user__in=following_users) |
            Q(user=self.request.user)).order_by("-timestamp")
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
